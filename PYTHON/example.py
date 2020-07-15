import datetime
from datetime import timedelta
from dateutil.parser import parse
from pprint import pprint
import boto3
import boto3



client = boto3.client('ec2')
response = client.create_tags(

    Resources=[
        'snap-09b96f4ddd6f5666f'
    ],
    Tags=[
        {
            'Key':'this is a test',
            'Value':'from vscode'
        },
    ]

)
