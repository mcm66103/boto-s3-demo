import os
import logging

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv() # configure environment variables from .env file

def get_client():
    """
    Prepare Boto s3 client with acccess key and secret key from .
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("ACCESS_KEY"),
        aws_secret_access_key=os.getenv("SECRET_KEY")
    )
    return s3

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = get_client()
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file("test_media.gif", os.getenv("BUCKET_NAME"))
