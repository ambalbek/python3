#!/usr/bin/env python3
from datetime import datetime, timedelta
import boto3 , datetime, csv
from operator import itemgetter
from time_differance_module import time_diff
from csv_module import csv_creator
    
def lambda_handler():
    ec2_client=boto3.client('ec2')
    snapshots=ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    total = 0
    lst=[]
    sorted_vlm=[]
    for i in snapshots:
        
        snap_id=i['SnapshotId']
        starttime=i['StartTime']
        volumesize=i['VolumeSize']
        #sorted_vlm.append(volumesize)
        #print(sorted_vlm)
        total+=volumesize
        if time_diff(starttime) >=0:
            final=dict()
            total_6m=0
            total_6m+=volumesize
            final['Snapshot_id']=snap_id
            #final['start_time']=starttime
            #final['volume_size_total']=total_6m
            final['days']=time_diff(starttime)
            final['volume_size']=volumesize
            lst.append(final)
            #print(final)
            #return final
            #print(final)
    return csv_creator(lst)
lambda_handler()
#account_id(listDict)
