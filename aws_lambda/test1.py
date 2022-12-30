#!/usr/bin/env python3
# Description: Lambda for rescheduling the EC2 events to weekend in case they are received over weekdays.
# The function process the event, computes next weekend outage to reschedule the event.
# After rescheduling event it sends SNS notification.


import boto3
import pandas as pd
from botocore.exceptions import ClientError
import logging
from datetime import datetime, timedelta
from botocore.config import Config
import os

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

EVENT_SNS_TOPIC_ARN = os.environ['EVENT_SNS_TOPIC_ARN']  # Read SNS Topic ARN from lambda environment variables
DAY_OF_WEEK = os.environ['DAY_OF_WEEK']  # Week day of Local maintenance Date (Mon=0, Tue=1, .., Sat=5, Sun=6)

config = Config(retries=dict(max_attempts=3, mode='standard'))
ec2_client = boto3.client('ec2', config=config)
sns_client = boto3.client('sns', config=config)

# Function to process event rescheduling. If the AWS event is already schedule on weekend, the schedule is unchanged .
# Otherwise, the function computes the next weekend date (Saturday) and returns new schedule


def get_weekend_schedule_start_time(aws_event_schedule):
    # Return Data: Rescheduled Flag to check if event is rescheduled and reschedule date
    try:
        current_date = datetime.now().replace(tzinfo=aws_event_schedule.tzinfo, minute=00, hour=00, second=00)
        current_weekday = current_date.weekday()  # Current weekday
        upcoming_weekend = current_date + timedelta(days=(int(DAY_OF_WEEK) - current_weekday))  # Coming Saturday
        next_weekend = upcoming_weekend + timedelta(days=7)  # Next Saturday
        weekend_span = 7 - int(DAY_OF_WEEK)
        # Event is after coming monday and before next Saturday
        if upcoming_weekend + timedelta(days=weekend_span) < aws_event_schedule < next_weekend:
            return True, upcoming_weekend
        # Event is after next-next monday
        elif aws_event_schedule > (next_weekend + timedelta(days=weekend_span)):
            return True, next_weekend
        else:
            return False, aws_event_schedule
    except Exception as ex:
        logger.error('There was error in computing the reschedule date.\n{}'.format(ex))
        return False, aws_event_schedule


def describe_instance_status(instance_id):
    flag = False
    instance_event_id = []
    try:
        response = ec2_client.describe_instance_status(
            InstanceIds=[
                instance_id,
            ]
        )
        if response:
            logger.info("response is====> %s", response)
            if 'InstanceStatuses' in response:
                logger.info("InstanceStatuses is====> %s", response['InstanceStatuses'])
                for instance_status in response['InstanceStatuses']:
                    if 'Events' in instance_status:
                        logger.info("events are is====> %s", instance_status['Events'])
                        for event in instance_status['Events']:
                            logger.info("event is %s", event)
                            instance_event_id.append(event['InstanceEventId'])
                            flag = True
    except Exception as ex:
        logger.error("Exception while changing the instance schedule - %s", ex)
    logger.info("returning response=======> flag: %s   instance_event_id: %s", flag, instance_event_id)
    return flag, instance_event_id


def publish_sns_topic(sns_instance_id, sns_event_date, sns_aws_account):
    sns_subject = 'AWS EC2 maintenance required for {} associated with your AWS Account:{}'.\
        format(sns_instance_id, sns_aws_account)
    sns_message = '''Action: Stop and start for EC2 underlying hardware event\n\n{} will undergo a stop and start around {} in the AWS account {}, during which your instance will be stopped and started.\n\nIf you do not want to wait until the event scheduled time, please manually stop and start the instance when convenient.'''.format(
        sns_instance_id,
        sns_event_date,
        sns_aws_account
    )
    try:
        sns_client.publish(
            TopicArn=EVENT_SNS_TOPIC_ARN,
            Subject=sns_subject,
            Message=sns_message
        )
        logger.info('SNS Topic Published Successfully')
    except Exception as e:
        logger.error('SNS Topic Publish failed with error.\n{}'.format(e))



def lambda_handler(event, context):
    # Read received events, Validate environment variables and Event Parameter Values
    logger.info("event received %s, %s", event, context)
    for i in event:
        aws_account = i['account']
        start_time = i['detail']['startTime']
        instance_id_list = i['resources']
        
        try:
            delimited_instance_list = ', '.join(instance_id_list)
            # Convert received event schedule received as string to datetime
            scheduled_event_date = pd.to_datetime(start_time)
            # Call function to check if rescheduling is needed and receive new event date if applicable
            rescheduling_flag, weekend_start_time = get_weekend_schedule_start_time(scheduled_event_date)
            # If the event schedule and proposed schedule are different, reschedule to the event and notify the users
            if rescheduling_flag:
                logger.info('The event will be rescheduled to {}'.format(weekend_start_time))
                # Iterate over all ec2 instances received in the event
                logging.info("Starting the for loop for list: %s", delimited_instance_list)
                for instance_id in instance_id_list:
                    logging.info("instance_id is %s", instance_id)
                    try:
                        flag, event_id_list = describe_instance_status(instance_id)
                        # Attempt to change to the event by making call to AWS with rescheduled event date
                        if flag:
                            for event_id in event_id_list:
                                ec2_client.modify_instance_event_start_time(
                                  DryRun=False,
                                  InstanceId=instance_id,
                                  InstanceEventId=event_id,
                                  NotBefore=weekend_start_time
                                )
                            publish_sns_topic(instance_id, weekend_start_time, aws_account)
                        else:
                            publish_sns_topic(instance_id, start_time, aws_account)
                    except ClientError as e:
                        logger.error("There was an internal error while rescheduling the event. "
                                     "Error Message: %s Please check the logs", e)
                        logger.error("Publishing the message with the original date due to the above error")
                        publish_sns_topic(instance_id, start_time, aws_account)
                    except Exception as e:
                        # Error while Calling AWS to change event.
                        logger.error("There was an error while rescheduling the event %s.Please check the logs", e)
                        publish_sns_topic(instance_id, start_time, aws_account)
            else:
                # The Event date is unchanged. Log the event and notify the users
                logger.info("The event date is unchanged - {}".format(start_time))
                publish_sns_topic(delimited_instance_list, start_time, aws_account)
        except Exception as e:
            # Error while Calling AWS to change event.
            logger.error("There was an error while rescheduling the event %s.Please check the logs", e)
            publish_sns_topic(instance_id_list, start_time, aws_account)
