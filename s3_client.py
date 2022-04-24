import logging

import boto3
from botocore.exceptions import ClientError

import credentials


s3 = boto3.client('s3',
                  aws_access_key_id=credentials.aws_access_key_id,
                  aws_secret_access_key=credentials.aws_secret_access_key)


INPUT_BUCKET = 'input-videostorage'
OUTPUT_BUCKET = 'output-videostorage'


def upload_fileobject(file, object_name):

    try:
        s3.upload_fileobj(file, INPUT_BUCKET, object_name)

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


def download_files(source_filename):

    file_name = source_filename.rsplit('.', 1)[0]
    file_extension = source_filename.rsplit('.', 1)[1]

    postfixes = ['_1920x1080.', '_1080x1920.', '_1080x1350.']
    for postfix in postfixes:
        filename = file_name + postfix + file_extension
        download_file(filename)
