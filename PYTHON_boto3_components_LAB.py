# Author: Hemant Gangwar
# Role: This script will make use of boto3 components

# Variables to be substituted :
# <your_profile_name> 			= Profile name if any in your aws credential files
# <your_region> 				= Default region you want to work with
# <your_bucket_name> 			= Custom name of your bucket
# <your_ami_id> 				= AMI ID for building EC2
# <your_instance_hw_type> 		= Hardware type for EC2 instance
# <your_key_name> 			= Custom key to create and connect EC2 with
# <your_list_of_security_groups> 	= List of security groups to be used

import boto3


# Setting session credentials explicitely to authenticate #
aws_session = boto3.session.Session(profile_name='<your_profile_name>', 
             region_name='<your_region>')

#print(dir(aws_session))

# Uncomment below if you want to see all available resources by session component #
# print(aws_session.get_available_resources())

# Starting with client operations #
s3_ops = aws_session.client('s3')

# Uncomment only if you want to create new bucket #
# response = s3_ops.create_bucket(Bucket='<your_bucket_name>', CreateBucketConfiguration={'LocationConstraint': '<your_region>'})
# print(response)

# Uncomment if you want to list available buckets in your provided region #
#list_bucket_response = s3_ops.list_buckets()
#bucket_list = list_bucket_response['Buckets']
for buckets in bucket_list:
    print(buckets['Name'])

# Starting with Resource level operations #
ec2_ops = aws_session.resource('ec2')

# Uncomment below if you want to create a new EC2 #
#my_custom_ec2 = ec2_ops.create_instances(
#    ImageId='<your_ami_id>',
#    MinCount=1,
#    MaxCount=1,
#    InstanceType="<your_instance_hw_type>",
#    KeyName='<your_key_name>',
#    SecurityGroupIds=['<your_list_of_security_groups>'],
#    Placement={
#            'AvailabilityZone': '<your_region>',
#            'Tenancy': 'default',
#            },
#    TagSpecifications=[
#        {
#            'ResourceType': 'instance',
#            'Tags': [
#                {
#                    'Key': 'Name',
#                    'Value': 'My_Python-Ec2'
#                },
#            ]
#        },
#        ],
#)

# print(my_custom_ec2)