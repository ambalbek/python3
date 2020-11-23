import boto3, time
from pprint import pprint
iam=boto3.client('iam')
ec2=boto3.client('ec2')
users=iam.list_users()['Users']
instances=ec2.describe_instances()['Reservations']
waiter = ec2.get_waiter('instance_running')
'''
#print(users)
for i in users:
    print(i.get('UserName'),i.get('UserId'),i.get('CreateDate'), sep=' - ')
'''
for instance in instances:
    
    for i in instance['Instances']:
        ec2_id=i.get('InstanceId')
        state=i.get('State')['Name']
        stop_instances=ec2.start_instances(InstanceIds=[ec2_id])
        waiting=waiter.wait(InstanceIds=[ec2_id])
        print(ec2_id,'instace starting....',state)
        #pprint(instance['Instances'])
        '''
        while True:
            if state=='running':
                ec2.stop_instances(InstanceIds=[ec2_id])
                print(ec2_id,'instace stoping....')
                break
            #time.sleep(10)



    
    for a in instance['Instances']:
        ec2_id=a.get('InstanceId')
        stop_instances=ec2.stop_instances(InstanceIds=[ec2_id])
        waiting=waiter.wait(InstanceIds=[ec2_id])
        print(ec2_id,'instace stoping....')
    '''
