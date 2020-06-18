import datetime
from dateutil.parser import parse
from pprint import pprint
from time_differance_module import time_diff
import boto3

def lambda_handler():#(event, context):
    ec2=boto3.client('ec2')
    instances=ec2.describe_instances()['Reservations']
    for i in instances:
        for x in i['Instances']:
            pprint(x)
lambda_handler()