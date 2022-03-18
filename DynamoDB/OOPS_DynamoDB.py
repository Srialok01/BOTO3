try:
    import boto3
    from botocore.exceptions import ClientError

    print("All modules loaded ....")
except Exception as e:
    print("Error.{}".format(e))


class MyDB:
    def __init__(self, Table_Name='Movies'):
        self.table_name = Table_Name
        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(self.table_name)
        self.client = boto3.client('dynamodb')

    def create_item(self, title, year, ott_platform):
        print("+++++++++ Inside CREATE Item +++++++++")
        self.year = year
        self.title = title
        self.ott_platform = ott_platform
        try:
            response = self.table.put_item(
                Item={
                    'year': self.year,
                    'title': self.title,
                    'ott_platform': self.ott_platform
                }
            )
        except Exception as e:
            print(e.response['Error']['Message'])

        else:
            return response

    def read_item(self, title, year):
        print("\n+++++++++ Inside READ Item +++++++++\n")
        self.title = title
        self.year = year
        try:
            response = self.table.get_item(
                Key={
                    'title': self.title,
                    'year': self.year
                }
            )

        except ClientError as e:
            print(e.response['Error']['Message'])

        else:
            return response

    def update_item(self, title, year, new_ott):
        print("\n+++++++++ Inside UPDATE Item +++++++++\n")
        self.year = year
        self.title = title
        self.new_ott = new_ott
        try:

            response = self.table.update_item(
                Key={
                    'year': self.year,
                    'title': self.title
                },
                UpdateExpression="set ott_platform= :v1",
                ExpressionAttributeValues={
                    ':v1': self.new_ott
                }
            )
        except Exception as e:
            print(e.response['Error']['Message'])

        else:
            return "Resource Updated"

    def delete_item(self, title, year):
        print("\n+++++++++ Inside DELETE Item +++++++++\n")
        self.year = year
        self.title = title
        self.table.delete_item(
            Key={
                'year': self.year,
                'title': self.title
            }
        )
        return 'resource deleted'

    def describe_table(self, tableName):
        print("\n+++++++++ Inside Describe table method +++++++++\n")
        self.tableName = tableName
        try:
            table_description = self.client.describe_table(
                TableName=self.tableName
            )
            status_response_code = table_description['ResponseMetadata'].get('HTTPStatusCode')
            assert status_response_code == 200, "Error in retrieving response from aws"
        except Exception as e:
            print(e.response['Error']['Message'])
        else:
            return table_description


if __name__ == '__main__':
    table_name = 'Movies'
    obj = MyDB()
    response = obj.describe_table(table_name)
    table = response['Table'].get('TableName')
    print(f"The name of the table is {table}\n")
    assert table == table_name, f"Employees Table doesn't exists !!"

    # Creating a record in dynamo db
    obj.create_item('BatMan', 2021, 'Disney+Hotstar')

    # Reading the created record in dynamo db
    resp = obj.read_item('BatMan', 2021)
    assert resp['Item'].get('title') == 'BatMan', 'record not present in Dynamo DB'

    obj.update_item('BatMan', 2021, 'MX Player')
    resp = obj.read_item('BatMan', 2021)
    assert resp['Item'].get('title') == 'BatMan', 'record not present in Dynamo DB'

    obj.delete_item('BatMan', 2021)
    resp = obj.read_item('BatMan', 2021)
    try:
        title = resp['Item'].get('title')
        assert title != 'BatMan', 'record not present in Dynamo DB'
    except KeyError as e:
        print('The title Batman is not found ')
