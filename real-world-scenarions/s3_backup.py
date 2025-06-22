"""
This is script to take a backup from local to AWS S3
boto3--> Used to do AWS tasks using python
"""
import logging
import boto3
from botocore.exceptions import ClientError
import shutil
import datetime
import os

s3 = boto3.client('s3',region_name="us-east-1")
region="us-west-2"
bucket_name="backet-name"

#Show buckets from AWS S3
def show_buckets(s3):
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

#Create a bucket in the specified region
def create_bucket(bucket_name):
    # Create bucket
    try:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#Upload the backup file into the S3 bucket
def upload_files(s,d):
    s3.upload_file(s, "bucket-name", d)
    
#Take backup of files on daily basis
def backup_files(source,destination):
    today=datetime.date.today()
    file_name=f"backup_{today}"
    backup_file_name=os.path.join(destination,file_name)
    shutil.make_archive(backup_file_name,'gztar',source)
    bucket_status=create_bucket(bucket_name)
    if bucket_status == True:
        upload_files(f"{backup_file_name}.tar.gz",f"{file_name}.tar.gz")


#Call backup_files function
source="source-path"
destination="destination-path"
backup_files(source,destination)
show_buckets(s3)