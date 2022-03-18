import boto3
import glob

client = boto3.client('s3')


def upload(filename, bucket, objectname=None, args=None):
    if objectname == None:
        objectname = filename

    resp = client.upload_file(filename, bucket, objectname, ExtraArgs=args)
    return resp


# Upload single file
# response = upload(filename='upload_files/sample_load.json', bucket='alok6032022')

## Upload multiple files

files = glob.glob('upload_files/*')
args = {'ACL': 'public-read'}
for file in files:
    resp =upload(filename=file, bucket='alok6032022', args=args)
    print(resp)
