import json
import boto3

import credentials


mediaconvert = boto3.client('mediaconvert',
                            aws_access_key_id=credentials.aws_access_key_id,
                            aws_secret_access_key=credentials.aws_secret_access_key,
                            region_name='eu-west-1',
                            endpoint_url=credentials.aws_mediaconvert_endpoint)


def make_settings(file_name, cut_start, cut_end):
    """create .json job settings from template"""

    with open('job_templates/cut_and_resize.json', 'r') as f:
        settings = json.load(f)

    file_path = 's3://input-videostorage/' + file_name
    settings['Settings']['Inputs'][0]['FileInput'] = file_path
    settings['Settings']['Inputs'][0]['InputClippings'][0]['StartTimecode'] = '00:00:{};00'.format(cut_start)
    settings['Settings']['Inputs'][0]['InputClippings'][0]['EndTimecode'] = '00:00:{};00'.format(cut_end)

    return settings


def create_job(file_name, cut_start, cut_end):
    settings = make_settings(file_name, cut_start, cut_end)

    mediaconvert.create_job(**settings)


def list_jobs():
    response = mediaconvert.list_jobs(
        MaxResults=10,
        Order='DESCENDING'
    )

    return response
