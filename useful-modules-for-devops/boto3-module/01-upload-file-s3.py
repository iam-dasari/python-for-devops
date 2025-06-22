import boto3

s3 = boto3.client('s3')

s3.upload_file('hello.txt', 'bucket-name', 'hello.txt') #Replace bucket-name with your AWS S3 bucket name

#ACCESS KEY, SECRET ACCESS KEY, REGION can be entered using "aws configure"