#!/usr/bin/env python3
import boto3, parser
from csv_module import csv_creator
from time_differance_module import time_diff
def sg():
      list_sg=[]
      ec2=boto3.client('ec2')
      response = ec2.describe_security_groups()['SecurityGroups']
      for i in response:
            sg_dict=dict()
            sg_dict['sg_name']=i['GroupName']
            sg_dict['sg_id']=i['GroupId']
            list_sg.append(sg_dict)
      return csv_creator(list_sg)
            
      
            
      #return csv_creator(list_sg)
sg()