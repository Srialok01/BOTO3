try:
    import boto3
    from botocore.exceptions import ClientError
    import glob

    print("All modules loaded ....")
except Exception as e:
    print("Error.{}".format(e))


class AmazonS3:
    def __init__(self, Bucket_Name):
        self.bucket_name = Bucket_Name
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')
        self.s3_location = "us-east-2"

    def list_objects(self,Bucket):
        try:
            response = self.s3_client.list_objects(Bucket=Bucket)
            assert response['ResponseMetadata']['HTTPStatusCode'] == 200, "Unable to retrieve total objects"

        except Exception as e:
            print(e.response['Error']['Message'])

        else:
            obj_list = [i.get('Key') for i in response['Contents']]
            return obj_list

    def create_bucket(self):
        print("+++++++++ INSIDE CREATE BUCKET +++++++++")
        try:
            resp = self.s3_client.create_bucket(ACL='public-read-write',
                                                Bucket=self.bucket_name,
                                                CreateBucketConfiguration={'LocationConstraint': self.s3_location})
        except Exception as e:
            print(e.response['Error']['Message'])

        else:
            assert resp['ResponseMetadata']['HTTPStatusCode'] == 200, "Unable to create a bucket"

    def list_bucket(self):
        print("+++++++++ INSIDE LIST BUCKET +++++++++")
        try:
            response = self.s3_client.list_buckets()
        except Exception as e:
            print(e.response['Error']['Message'])

        else:
            assert response['ResponseMetadata']['HTTPStatusCode'] == 200, "Unable to retrieve a bucket"
            for bucket in response['Buckets']:
                assert bucket['Name'] == self.bucket_name, "Bucket name is different in response"

    def upload_files(self, FileName, Bucket, ObjectName=None, args=None):
        print("+++++++++ INSIDE UPLOAD FILES +++++++++")
        if ObjectName is None:
            ObjectName = FileName
        try:
            resp = self.s3_client.upload_file(FileName, Bucket, ObjectName, ExtraArgs=args)
            assert resp is None, "Error in uploading file"

        except Exception as e:
            print("Exception")
            print(e.response['Error']['Message'])

        else:
            print(f'File {FileName} is uploaded successfully !!')

    def download_files(self, Bucket):
        print("+++++++++ INSIDE DOWNLOAD FILES +++++++++")
        files_list = self.list_objects(Bucket=Bucket)
        for file in files_list:
            self.s3_resource.meta.client.download_file(self.bucket_name, file, file)
            print(f"File {file} downloaded")

    def delete_bucket(self, Bucket):
        print("+++++++++ INSIDE DELETE BUCKET +++++++++")
        files_list = self.list_objects(Bucket=Bucket)
        for file in files_list:
            self.s3_client.delete_object(Bucket=Bucket, Key=file)
        resp = self.s3_client.delete_bucket(Bucket=Bucket)
        assert resp['ResponseMetadata']['HTTPStatusCode'] == 204, "Unable to delete a bucket"
        print(f"Bucket {Bucket} deleted successfully !!")


if __name__ == '__main__':
    bucket_name = 'alok18032022'
    files_path = 'upload_files/*'
    obj = AmazonS3(bucket_name)

    obj.create_bucket()

    obj.list_bucket()

    files = glob.glob(files_path)
    if not files:
        raise FileNotFoundError('upload files not found')
    else:
        for file in files:
            obj.upload_files(file, bucket_name)

    obj.download_files(bucket_name)

    obj.delete_bucket(bucket_name)
