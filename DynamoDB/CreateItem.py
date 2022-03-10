import boto3


def create_item(year, title, ott_platform):
    client = boto3.resource('dynamodb')
    table = client.Table('Movies')
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'ott_platform': ott_platform
        }
    )
    return response


if __name__ == '__main__':
    movies_resp = create_item(2021, 'BatMan', 'Disney+Hotstar')
    print(movies_resp)
    status_code = movies_resp['ResponseMetadata'].get('HTTPStatusCode')
    assert status_code == 200, "Error in retrieving response from aws"
