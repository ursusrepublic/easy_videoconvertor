# https://docs.aws.amazon.com/mediaconvert/latest/apireference/endpoints.html
import boto3
import credentials


client = boto3.client('mediaconvert',
                      aws_access_key_id=credentials.aws_access_key_id,
                      aws_secret_access_key=credentials.aws_secret_access_key,
                      region_name='eu-west-1')

response = client.describe_endpoints(
    MaxResults=123,
    Mode='DEFAULT'
)

print(response)
