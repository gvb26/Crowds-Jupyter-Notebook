import boto3
import decimal
import populartimes

api_key = 'AIzaSyCbzq7OEa1W-Tszf7nmWb7F9zXMLsyYv94'
types = ["bar", "restaurant"]
bound_lower = (39.953434, -75.164337)
bound_upper = (39.968697, -75.203133)
data = []
businesses = []

if __name__ == '__main__':
    data = populartimes.get(api_key, ["bar", "restaurant"], bound_lower, bound_upper)
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='Businesses',
        KeySchema=[
            {
                'AttributeName': 'Business',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'ID',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Business',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'ID',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Address',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'CrowdSize',
                'AttributeType': 'S'
            }            
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='Businesses')

    # for name in data:
    #     try:
    #         business = name['name']    
    #         id = name['id']
    #         populartimes = name['populartimes']
    #         rating = name['rating']
    #         newObj = Business(business, id, populartimes, name['rating'])
            
    #     except KeyError:
    #         print("Key not found")
    #         pass

    #     businesses.append(newObj)

    # df = pd.DataFrame(data)

    # for business in businesses:
    #     if business.id == 'ChIJCW75x1HGxokR3vEgaoFQKsw':
    #         print(business.name)
    #         print(business.getAllCrowdSize('Monday'))
    #         print(business.getCrowdSizeByHour('Monday', 1))
    