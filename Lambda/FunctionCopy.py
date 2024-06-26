
# This is a python code this get run when a event get triggered Lambda function code
# when every a new oject placed on source S3 bucket event trigger lambda function and copy to destination S3 bucket

import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the source and destination bucket names
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    destination_bucket = 'YOUR_DESTINATION_BUCKET_NAME'
    
    # Get the key (filename) of the uploaded file
    object_key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Copy the object from source bucket to destination bucket
        copy_source = {'Bucket': source_bucket, 'Key': object_key}
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=object_key)
        
        print(f'File {object_key} copied from {source_bucket} to {destination_bucket}')
        
        return {
            'statusCode': 200,
            'body': 'File copied successfully'
        }
    except Exception as e:
        print(f'Error copying file: {e}')
        return {
            'statusCode': 500,
            'body': 'Error copying file'
        }