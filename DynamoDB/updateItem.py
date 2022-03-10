import boto3

def update_item(year, title, new_ott):
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('Movies')
    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set ott_platform= :v1",
        ExpressionAttributeValues={
            ':v1': new_ott
        }
    )
    return "Updated"


if __name__ == "__main__":
    resp = update_item(2021, 'BatMan', 'MX Player')
    print(resp)


