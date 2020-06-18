import boto3

s3=boto3.resource('s3')
response = s3.delete_bucket(Bucket='ambalbek')
print(response)