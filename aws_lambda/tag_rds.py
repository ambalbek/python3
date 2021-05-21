import boto3
from datetime import datetime
from datetime import timedelta
from pprint import pprint
rds_client = boto3.client('rds')
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')   
def lambda_handler(event, context):
    count = 0
    response = s3_client.list_buckets()
    bucket_list = [i for i in response['Buckets']]
    for bucket in bucket_list:
        count +=1
        bucket_tagging = s3.BucketTagging(bucket['Name'])
        tags = bucket_tagging.tag_set
        tags.append({'Key':'Owner', 'Value': owner})
        Set_Tag = bucket_tagging.put(Tagging={'Tag':tags})
        print(Set_Tag)
        # print(count,bucket['Name'], bucket['CreationDate'].strftime("%b/%d/%Y"), sep=(', '))
