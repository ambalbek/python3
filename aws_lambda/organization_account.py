#!/usr/bin/env python3
from threading import current_thread
import boto3
from botocore.exceptions import ClientError
import logging
# from datetime import datetime
# from datetime import timedelta
from botocore.config import Config
from pprint import pprint
def lambda_handler(event, context):
    accounts = []
    org_client = boto3.client('organizations')
    paginator = org_client.get_paginator('list_accounts')
    pages = paginator.paginate()
    dynamodb = boto3.resource('dynamodb')
    account_table = dynamodb.Table('table')
    table_scan = account_table.scan()['Items']
    for page in pages:
        for account in page['Accounts']:
            # print(page['Accounts'])
            # pprint(account)
            # pprint(account['JoinedTimestamp'].strftime("%d-%b-%Y %H:%M:%S"))
            dic={}
            dic['account'] = account['Id']
            dic['JoinedTimestamp'] = account['JoinedTimestamp'].strftime("%d-%b-%Y %H:%M:%S")
            dic['Email'] = account['Email']
            dic['Status'] = account['Status']
            dic['JoinedMethod'] = account['JoinedMethod']

            try:
             
                if dic != table_scan[0]:
                    with account_table.batch_writer() as batch:
                        batch.put_item(Item=dic)
                        print('updated')
                else:
                    print('its in the table')
            except Exception as ex:
                print(ex)