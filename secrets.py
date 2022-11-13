# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError

secret_name = "aws-iot/awshost"
region_name = "us-east-1"
    
#Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

def get_secret():

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name)

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    
    return secret



get_secret()
