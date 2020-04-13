# boto-s3-demo
Upload image to s3 bucket with python boto library.

## Prerequisites
Provision an S3 bucket and an IAM user with s3 full access.

## Requirements
```python
pip install -r requirements.txt
```
This demo uses boto3 and python-dotenv.

## Environment Variables
Before you run the script, configure the .env file with information about your IAM user and your S3 Bucket.

## Usage
```python
python main.py
```
Now check in your bucket. A new image is there.
