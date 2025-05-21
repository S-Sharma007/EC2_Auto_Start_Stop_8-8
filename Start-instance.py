import boto3
import logging
import os

def lambda_handler(event, context):
    # Initialize logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Get instance IDs from environment variables
    instance_ids = os.environ.get('EC2_INSTANCE_IDS', '').split(',')
    
    if not instance_ids or instance_ids[0] == '':
        error_msg = "No instance IDs configured in environment variables"
        logger.error(error_msg)
        return {
            'statusCode': 400,
            'body': error_msg
        }
    
    ec2 = boto3.client('ec2')
    try:
        response = ec2.start_instances(InstanceIds=instance_ids)
        logger.info(f"Started instances: {instance_ids}")
        return {
            'statusCode': 200,
            'body': f"Successfully started instances: {instance_ids}"
        }
    except Exception as e:
        logger.error(f"Error starting instances: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error starting instances: {str(e)}"
        }
