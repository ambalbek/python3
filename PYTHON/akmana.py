#!/usr/bin/env python3
import datetime
from dateutil.parser import parse
import csv
import boto3



def days_old(date):
    parsed = parse(date).replace(tzinfo=None)
    diff = datetime.datetime.now() - parsed
    return diff.days


def lambda_handler(event, context):

    x=[[v for ami.items() if k=='Name' and v!=v.startswith('DFS')]for ami in amis = ec2.describe_images(Owners=['self'])['Images']]

    for ami in amis:
        #print(ami)
        for k,v in ami.items():
            if k=='Name':
                print(v)
                
