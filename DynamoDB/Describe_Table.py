import boto3

client = boto3.client('dynamodb')
table_description = client.describe_table(
    TableName='Movies'
)
print(table_description)
status_response_code = table_description['ResponseMetadata'].get('HTTPStatusCode')
assert status_response_code == 200, "Error in retrieving response from aws"
table_name = table_description['Table'].get('TableName')
assert table_name == 'Movies', f"Employees Table doesn't exists !!"




