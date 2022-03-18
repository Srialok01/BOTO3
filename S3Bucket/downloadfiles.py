import boto3

# client = boto3.client('s3')
resource = boto3.resource('s3')

resp = resource.list_objects(Bucket='alok6032022')

for i in resp['Contents']:
    file = i.get('Key')
    resource.meta.client.download_file('alok6032022',file,file)
    print(f"File {file} downloaded")

