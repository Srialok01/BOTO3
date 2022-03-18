import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
print(response['Buckets'])
resp = s3.list_objects(Bucket='alok6032022')
try:

    for i in resp['Contents']:
        file = i.get('Key')
        s3.delete_object(Bucket='alok6032022', Key=file)
        print(f"File {file} deleted")
except:
    pass

resp = s3.delete_bucket(Bucket='alok6032022')
assert resp['HTTPStatusCode'] == 204
