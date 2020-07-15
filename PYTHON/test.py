import boto3
from pprint import pprint
from time_differance_module import time_diff
import datetime
session = boto3.session.Session()

def aws_iam():
    iam_cli=session.client('iam')
    '''
    for each_user in iam_cli.list_users()['Users']:
    print(cnt, each_user['UserName'], each_user['UserId'])

    '''
    cnt=0
    paginator = iam_cli.get_paginator('list_users')
    for each_page in paginator.paginate():
        for items in each_page['Users']:
            cnt+=1
            userid=items['UserId']
            username=items['UserName']
            createdate=items['CreateDate']
            print(cnt,'|',username,'|',userid,'|',time_diff(createdate),'days')
aws_iam()