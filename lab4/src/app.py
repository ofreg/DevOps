import boto3
import os

BUCKET_NAME = os.environ['BUCKET_NAME']
FILE_KEY = os.environ['FILE_KEY']

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
        data_bytes = obj['Body'].read()
        data_str = data_bytes.decode('utf-8')
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/plain'},
            'body': data_str
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
