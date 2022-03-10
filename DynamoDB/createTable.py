import boto3

# Get the service resource
dynamo_db = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamo_db.create_table(
    TableName='Movies',

    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # value can get duplicated {PARTITION KEY}
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Unique {sort key}
        }
    ],

    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'  # number attribute
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'  # string attribute
        }
    ],

    # allocate limits for RCU & WCU as it would charge based on the allocation done not on actual
    # used

    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

)

# Wait until table exists
table.wait_until_exists()

# Print out some data about the table
print(table.item_count)




