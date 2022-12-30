#!/usr/bin/env python3
import boto3, sys
def ec2():
    aws_mng_console=boto3.session.Session()
    ec2_console=aws_mng_console.resource("ec2")
    ec2_client=aws_mng_console.client("ec2")
    #opt=int(input("Enter your option: "))
    
    try:
        while True:
            opt=int(input("Enter your option from 1 to 4: "))
            print("This scripts perform following actions")
            print("""
                1. start
                2. stop
                3. terminate
                4. exit
                """)
            if opt == 1:
                instance_id=input("Enter your instance ID: ")
                instance_command=ec2_console.Instance(instance_id)
                #print(dir(instance_command))
                print("starting ec2 instance...", instance_id)
                instance_command.start()
                break
            elif opt==2:
                instance_id=input("Enter your instance ID: ")
                instance_command=ec2_console.Instance(instance_id)
                print("stoping ec2 instance...", instance_id)
                instance_command.stop()
                break
            elif opt==3:
                instance_id=input("Enter your instance ID: ")
                instance_command=ec2_console.Instance(instance_id)
                print("terminating ec2 instance..", instance_id)
                instance_command.terminate()
                break
            elif opt==4:
                print("Thank you for using this script")
                sys.exit()
                break
            
            else:
                print("Your option is invalid, Try again")
    except:
        print("You didnt choose the right option! Try again later")

ec2()
