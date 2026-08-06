import boto3
from datetime import datetime, timezone

ec2 = boto3.client("ec2")

response = ec2.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["stopped"]}]
)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        launch = instance["LaunchTime"]

        age = (datetime.now(timezone.utc) - launch).days

        if age > 30:
            print(f"Deleting {instance['InstanceId']}")
            ec2.terminate_instances(
                InstanceIds=[instance["InstanceId"]]
            )