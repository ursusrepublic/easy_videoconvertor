import json
import boto3

import credentials


converter = boto3.client('mediaconvert',
                         aws_access_key_id=credentials.aws_access_key_id,
                         aws_secret_access_key=credentials.aws_secret_access_key,
                         region_name='eu-west-1',
                         endpoint_url=credentials.aws_mediaconvert_endpoint)


def create_job(file_name, cut_start, cut_end):
    file_path = 's3://input-videostorage/' + file_name

    with open('job_templates/cutter.json', 'r') as f:
        template = json.load(f)

    template['Settings']['Inputs'][0]['FileInput'] = file_path
    template['Settings']['Inputs'][0]['InputClippings'][0]['StartTimecode'] = '00:00:{};00'.format(cut_start)
    template['Settings']['Inputs'][0]['InputClippings'][0]['EndTimecode'] = '00:00:{};00'.format(cut_end)

    converter.create_job(**template)
