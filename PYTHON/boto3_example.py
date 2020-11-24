import boto3
from pprint import pprint
ec2=boto3.client('ec2')
#This part is creating a ebs volume from snapshot_id
'''
response = ec2.create_volume(
    AvailabilityZone='us-east-1b',
    Encrypted=False,
    #Iops=100,
    #KmsKeyId='string',
    #OutpostArn='string',
    Size=8,
    SnapshotId='snap-0299d083f0ce6cd12',
    VolumeType='gp2',
    DryRun=False,
    TagSpecifications=[
        {
            'ResourceType':'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'from_lambda'
                },
            ]
        },
    ],
    MultiAttachEnabled=False
)

ebs = ec2.describe_volumes()['Volumes']
for i in ebs:
    ebs_id=i['VolumeId']
    print(ebs_id)
    
    try:
        delete_ebs_id = ec2.delete_volume(
            VolumeId=ebs_id,
            DryRun=False
        )
    except: pass
    print(ebs_id)
