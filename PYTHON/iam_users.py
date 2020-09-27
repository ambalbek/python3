import boto3
from csv_module import csv_creator
from time_differance_module import time_diff
ec2_client=boto3.client('ec2')
s3=boto3.client('s3')
iam=boto3.client('iam')
def accounts():
    list_users=[]
    responce=iam.list_users()
    for i in responce['Users']:
        username=i['UserName']
        userid=i['UserId']
        creation_date=i['CreateDate']
        if time_diff(creation_date) >= 0:
            account_dict=dict()
            account_dict['UserName']=username
            account_dict['UserId']=userid
            account_dict['Days']=time_diff(creation_date)
            list_users.append(account_dict)
            #print(account_dict)
    #return csv_creator(list_users)
    return (list_users)

def ami():
    list_ami=[]
    ami=ec2_client.describe_images(Owners=['self'])['Images']
    for i in ami:
        for a in i:
            final=dict()
            final['ami_id']=i['ImageId']
            final['owner_id']=i['OwnerId']
            final['ami_name']=i['Name']
    list_ami.append(final)
    print(list_ami)
    return csv_creator(list_ami)

accounts()
print(accounts())
#ami()
#csv_file(x)
