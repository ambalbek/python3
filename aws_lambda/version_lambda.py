#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError
import datetime
import logging
from datetime import datetime
from datetime import timedelta
from botocore.config import Config
import pandas as pd
import os
from dateutil.tz import tzlocal
from pprint import pprint
response_details=[{'event': {'arn': 'arn:aws:health:us-west-2::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_IHDCP_1607992032',
            'endTime': datetime.datetime(2020, 12, 14, 18, 55, 41, 959000, tzinfo=tzlocal()),        
            'eventScopeCode': 'PUBLIC',
            'eventTypeCategory': 'issue',
            'eventTypeCode': 'AWS_EC2_OPERATIONAL_ISSUE',
            'lastUpdatedTime': datetime.datetime(2020, 12, 14, 18, 55, 42, 278000, tzinfo=tzlocal()),
            'region': 'us-west-2',
            'service': 'EC2',
            'startTime': datetime.datetime(2020, 12, 14, 18, 27, 12, 673000, tzinfo=tzlocal()),      
            'statusCode': 'closed'},
  'eventDescription': {'latestDescription': '[RESOLVED] API Error Rates and '
                                            'Latencies\n'
                                            '\n'
                                            '[04:27 PM PST] We are '
                                            'investigating increased error '
                                            'rates and latencies for the EC2 '
                                            'APIs in the US-WEST-2 Region.\n'
                                            '\n'
                                            '[04:40 PM PST] We can confirm '
                                            'increased error rates and '
                                            'latencies for the EC2 '
                                            'network-related APIs and elevated '
                                            'launch failures for newly '
                                            'launched instances within the '
                                            'US-WEST-2 Region. We are working '
                                            'to resolve the issue.\n'
                                            '\n'
                                            '[04:46 PM PST] We are beginning '
                                            'to see signs of recovery with '
                                            'error rates and latencies '
                                            'returning to normal levels for '
                                            'the EC2 APIs in the US-WEST-2 '
                                            'Region. Launches of new instances '
                                            'are once again succeeding, and we '
                                            'continue to work towards full '
                                            'recovery.\n'
                                            '\n'
                                            '[04:55 PM PST] Between 4:05 PM '
                                            'and 4:39 PM PST, we experienced '
                                            'increased error rates and '
                                            'latencies for the EC2 APIs, and '
                                            'elevated launch failures for new '
                                            'EC2 instances in the US-WEST-2 '
                                            'Region. The issue has been '
                                            'resolved and the service is '
                                            'operating normally.'}}]

EVENT_SNS_TOPIC_ARN = os.environ['EVENT_SNS_TOPIC_ARN']  # Read SNS Topic ARN from lambda environment variables


config = Config(retries=dict(max_attempts=3, mode='standard'))
ec2_client = boto3.client('ec2', config=config)
sns_client = boto3.client('sns', config=config)


def lambda_handler(event, context):
    # response_details = event
    for event_details in response_details['successfulSet']:
        service = event_details['event']['service']
        event_type = event_details['event']['eventTypeCode']
        event_category = event_details['event']['eventTypeCategory']
        region = event_details['event']['region']
        availability_zone = event_details['event']['availabilityZone']
        start_time = event_details['event']['startTime'].strftime("%m/%d/%Y, %H:%M:%S")#.replace(', tzinfo=tzlocal()','')
        end_time = event_details['event']['endTime'].strftime("%m/%d/%Y, %H:%M:%S")#.replace(', tzinfo=tzlocal()','')
        last_updated = event_details['event']['lastUpdatedTime'].strftime("%m/%d/%Y, %H:%M:%S")#.replace(', tzinfo=tzlocal()','')
        status = event_details['event']['statusCode']
        event_scope = event_details['event']['eventScopeCode']
        event_description = event_details['eventDescription']['latestDescription']
        

        subject_sns = event_type
        html_body = '''This {} has occured with the below information details:.\n\t - Service \t {}\n\t - Event Type \t {}\n\t - Event Type Category \t {}\n\t - Region \t {}\n\t - Availibility Zone \t {}\n\t - Start Time \t {}\n\t - End Time \t {}\n\t - Last Updated Time \t {}\n\t - Status Code \t {}\n\t - Event Scope \t {}\n\t - Latest Description \t {}.'''.format(event_type,service,event_type,event_category,region,availability_zone,start_time,end_time,last_updated,status,event_scope,event_description)
        response_sns = sns_client.publish(TopicArn=EVENT_SNS_TOPIC_ARN, Subject = subject_sns, Message = html_body)