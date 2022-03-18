import boto3
client = boto3.client('s3')
resp =client.create_bucket(ACL='public-read-write',
                     Bucket ='alok6032022',
                     CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
print(resp)