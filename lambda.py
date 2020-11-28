import boto3, time
from random import choice
from pprint import pprint
iam=boto3.client('iam')
ec2=boto3.client('ec2')
sts=boto3.client('sts')
users=iam.list_users()['Users']
instances=ec2.describe_instances()['Reservations']
waiter = ec2.get_waiter('instance_running')
iam=boto3.resource('iam')
len_of_passwd=10
valid_chars_for_passwd='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
passwd=[choice(valid_chars_for_passwd) for i in range(len_of_passwd)]
print("".join(passwd))


# for user in iam.users.all():
#     print('______________')
#     print(user.user_name, user.create_date.strftime("%Y-%m-%d"), user.access_keys, user.attached_policies,sep=' - ')

""" #print(users)
for i in users:
    print(i.get('UserName'),i.get('UserId'),i.get('CreateDate'), sep=' - ')

    for instance in instances:
    
    for i in instance['Instances']:
        ec2_id=i.get('InstanceId')
        state=i.get('State')['Name']
        stop_instances=ec2.start_instances(InstanceIds=[ec2_id])
        waiting=waiter.wait(InstanceIds=[ec2_id])
        print(ec2_id,'instace starting....',state)
        #pprint(instance['Instances'])
        
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
    
sts_client=sts.get_caller_identity()
print(sts_client)
 """