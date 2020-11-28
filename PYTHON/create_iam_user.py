import boto3
from random import choice
def get_iam_client():
    iam_client=boto3.client('iam')
    return iam_client

def get_random_passwd():
    len_of_passwd=10
    valid_chars_for_passwd='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    try:
        passwd=[choice(valid_chars_for_passwd) for i in range(len_of_passwd)]
        return "".join(passwd)
    except:
        pass



def main():
    iam_client=get_iam_client()
    iam_username=#enter user name in string
    passwd=get_random_passwd()
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
    iam_client.create_user(UserName=iam_username)
    iam_client.create_login_profile(UserName=iam_username, Password=passwd, PasswordResetRequired=True)
    iam_client.attach_user_policy(UserName=iam_username, PolicyArn=PolicyArn)
    print('Iam username={} and password={}'.format(iam_username,passwd))
    return 'Iam username={} and password={}'.format(iam_username,passwd)
if __name__ == '__main__':
    main()