import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'cmps465-iam-2024001'
    key = 'sample.txt'
    
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    return {
        'statusCode': 200,
        'body': json.dumps({'file_content': content})
    }