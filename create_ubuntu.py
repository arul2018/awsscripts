#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')

user_data =  '''#!/bin/bash
apt update
apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa -y
apt update
apt install python3.7 -y
apt-get install python-pip -y
pip install --upgrade pip -y
'''

instance = ec2.create_instances(
 ImageId='ami-07c2e617785343806',
 KeyName='master_mar_14',
 MinCount=1,
 MaxCount=1,
 UserData=user_data,
 InstanceType='t2.medium')

print (instance[0].id)
