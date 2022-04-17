import os


aws_access_key_id = os.environ.get('AWSKEYID')
aws_secret_access_key = os.environ.get('AWSSECRETKEY')

# api endpoint is taken from utils.py, run utils.py only once
aws_mediaconvert_endpoint = os.environ.get('AWSCONVERTERENDPOINT')

print(aws_mediaconvert_endpoint)
