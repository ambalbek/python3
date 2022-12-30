#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError
import logging
from datetime import datetime, timedelta
from botocore.config import Config
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
config = Config(retries = dict(max_attempts = 3, mode = 'standard'))

EVENT_SNS_TOPIC_ARN = os.environ['EVENT_SNS_TOPIC_ARN']  # Read SNS Topic ARN from lambda environment variables

sns_client = boto3.client('sns', config=config)
health = boto3.client('health')


def lambda_handler(event, context):
    now = datetime.now()
    events_paginator = health.get_paginator('describe_events')
    
    # lets get data for last 7 days 
    
    try:
        response = events_paginator.paginate(
            filter={
                'startTimes': [
                    {
                        'from': datetime.now() - timedelta(minutes=30),
                        'to': datetime.now()
                    }
                ]
            },
            maxResults=100
        )
        response_details  = health.describe_event_details(eventArns = [response['arn']])
        for event_details in response_details['successfulSet']:
            events = event_details['event']
            event_describtion = event_details['eventDescription']
            
            html_body = """"""
            subject_sns = "Personal Health DashBoard Event "
            sns_client = boto3.client('sns', region_name= "us-east-1")
            html_body += event_describtion + ", "
            html_body += "\n"
            response_sns = sns_client.publish(TopicArn=EVENT_SNS_TOPIC_ARN, Subject = subject_sns, Message = html_body)
            logger.info("Email Sent! ==> %s", response_sns['MessageId'])
    except Exception as ex:
        logger.error("Exception raised==> %s", ex)