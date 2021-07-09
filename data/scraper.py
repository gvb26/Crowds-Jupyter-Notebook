import populartimes
import json
import csv
import pandas as pd
import boto3
from Object import Business

api_key = 'AIzaSyCbzq7OEa1W-Tszf7nmWb7F9zXMLsyYv94'
types = ["bar", "restaurant"]
bound_lower = (39.953434, -75.164337)
bound_upper = (39.968697, -75.203133)
data = []
businesses = []

def writeTable(name, id, address, crowdsize, ratings):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Businesses')
    response = table.put_item(
    Item={
        'Business': name,
        'ID': id,
        'Address': address,
        'Crowds': crowdsize,
        'Ratings': ratings
    }
    )
    print("PutItem succeeded:")

#populartimes.get(api_key, types, bound_lower, bound_upper, n_threads (opt), radius (opt), all_places (opt))
if __name__ == '__main__':
    data = populartimes.get(api_key, ["bar", "restaurant"], bound_lower, bound_upper)
    
    for name in data:
        try:
            business = name['name']    
            id = name['id']
            address = name['address']
            populartimes = name['populartimes']
            rating = name['rating']
            newObj = Business(business, id, address, populartimes, name['rating'])
            
        except KeyError:
            print("Key not found")
            pass

        businesses.append(newObj)

    df = pd.DataFrame(data)

    for business in businesses:
        writeTable(business.name, business.id, business.address, business.crowdsize, str(business.ratings))
        
    

    # df2 = df[df['id'] == 'ChIJCW75x1HGxokR3vEgaoFQKsw']

    # df3 = df2['populartimes'].apply(pd.Series))

    # print(df3.name)
    
    # with open('landmark.csv', 'wb') as file:
    #     #let w represent our file
    #     w = csv.writer(file)

    #     #write the header row
    #     w.writerow(["name", "address", "Monday"])
        