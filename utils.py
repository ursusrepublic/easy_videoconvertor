# https://docs.aws.amazon.com/mediaconvert/latest/apireference/endpoints.html
# run this script only once to get the endpoint url for credentials.py
import boto3
import credentials


client = boto3.client('mediaconvert',
                      aws_access_key_id=credentials.aws_access_key_id,
                      aws_secret_access_key=credentials.aws_secret_access_key,
                      region_name='eu-west-1')

res = client.describe_endpoints(Mode='DEFAULT')
endpoint_url = res['Endpoints'][0]['Url']

print(endpoint_url)
