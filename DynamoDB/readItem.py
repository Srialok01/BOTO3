import boto3
from botocore.exceptions import ClientError

def get_movie(title, year):
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('Movies')

    try:
        response = table.get_item(
            Key={
                'title': title,
                'year': year
            }
        )

    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        return response['Item']


print(get_movie('BatMan', 2021))



