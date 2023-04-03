import boto3
import argparse

AWS_CONN = boto3.session.Session(profile_name='devs', region_name='ap-south-1')
EC2_CLIENT = AWS_CONN.client('ec2', region_name='ap-south-1')
EC2_RESOURCE = AWS_CONN.resource('ec2')
EC2_DETAILS = EC2_CLIENT.describe_instances()

def create_snapshot():
        for reservation_detail in EC2_DETAILS['Reservations']:
            for instance in reservation_detail['Instances']:
                aws_instance_id = instance['InstanceId']
                aws_instance_root_device = instance['BlockDeviceMappings'][0]['Ebs']['VolumeId'] 

                snapshot = EC2_RESOURCE.create_snapshot(
                    VolumeId=aws_instance_root_device,
                    TagSpecifications=[
                        {
                            'ResourceType': 'snapshot',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': f'Snapshots-{aws_instance_id}-{aws_instance_root_device}'
                                },
                            ]
                    
                        },
                    ],
                )
                print("Snapshot captured ", "for EC2: ", aws_instance_id, "is ", snapshot.id )

def listing_snapshot():
        list_snapshot = EC2_CLIENT.describe_snapshots(OwnerIds=['self'])['Snapshots']

        print("generating current list of snapshots")

        # print(list_snapshot)
        print("SnapshotID\t\t StartTime\t\t\t State\t\t VolumeId\t\t")
        for snapshot in list_snapshot:
            print(snapshot['SnapshotId'], "|", snapshot['StartTime'], "|", snapshot['State'], "|", snapshot['VolumeId'] ) 

def delete_snapshots():    
        delete_snapshots = EC2_CLIENT.describe_snapshots(OwnerIds=['self'])['Snapshots']
        for snapshots in delete_snapshots:
            print("Deleting snapshot: ", snapshots['SnapshotId'])
            del_snapshot = EC2_CLIENT.delete_snapshot(
                    SnapshotId=snapshots['SnapshotId']
            )

parser = argparse.ArgumentParser(description='Understanding usage of snapshot script')
parser.add_argument("action", help="""Valid operations Include ===>
                    create_snap: Snapshot capture,
                    list_snap: Snapshot listing
                    delete_snap: Snapshot deletion.
                    """)
args = parser.parse_args()

if args.action == 'create_snap':
      create_snapshot()
      listing_snapshot()
elif args.action == 'list_snap':
      listing_snapshot()
elif args.action == 'delete_snap':
      delete_snapshots()
else:
      print("No Valid Operations provided. Thank You!!!")
