import boto3, datetime ,sys
import sys, json, threading
from pprint import pprint
def time_diff(snapcreated):
    now= datetime.datetime.now(datetime.timezone.utc)
    diff = now - snapcreated
    return diff.days
def lambda_handler():
    ec2_client=boto3.client('ec2')
    snapshots=ec2_client.describe_snapshots(OwnerIds=['self'])#['Snapshots']
    pprint(snapshots)
    '''
    total=[]
    for i in snapshots:
        snap_id=i['SnapshotId']
        starttime=i['StartTime']
        volumesize=i['VolumeSize']
        if time_diff(starttime) >= 0:
            final=dict()
            final['Snapshot_id']=snap_id
            #final['start_time']=starttime
            #final['volume_size']=volumesize
            final['days']=time_diff(starttime)
            #final['total_volume']=total
            total.append(final)
    #pprint(total)
    return total
'''
'''              
def account_id(snapshots, snapshot_result=[]):
    csv_list= snapshot_result
    csv_columns = csv_list[0]
    csv_file='snapshots.csv'
    try:
        with open(csv_file, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for entry in csv_list:
                writer.writerow(entry)
    except IOError as e:
        print('I/O error({0}):{1}'.format(e.errno, e.strerror))
    except:
        print('Unexpected error:', sys.exc_info()[0])
'''

lambda_handler()
