import logging

import boto3
from botocore.exceptions import ClientError

import credentials


s3 = boto3.client('s3',
                  aws_access_key_id=credentials.aws_access_key_id,
                  aws_secret_access_key=credentials.aws_secret_access_key)


INPUT_BUCKET = 'input-videostorage'
OUTPUT_BUCKET = 'output-videostorage'


def upload_file(file_name):

    try:
        s3.upload_file(
            Bucket=INPUT_BUCKET,
            Filename=file_name,
            Key=file_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(object_name):

    try:
        s3.download_file(
            Bucket=OUTPUT_BUCKET,
            Key=object_name,
            Filename=object_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True
