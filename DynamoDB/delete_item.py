import boto3


def delete_item(year, title):
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('Movies')
    table.delete_item(
        Key={
            'year': year,
            'title': title
        }
    )
    return 'resource deleted'


if __name__=="__main__":
    print(delete_item(2013, 'Rush'))