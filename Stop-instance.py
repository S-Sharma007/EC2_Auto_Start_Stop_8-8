import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_ids = ['i-0123456789abcdef0', 'i-0abcdef1234567890']  # Replace with real instance IDs

    try:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")
    except Exception as e:
        print(f"Error stopping instances: {str(e)}")
