import populartimes
import json
import pandas as pd

data = []

if __name__ == '__main__':
    data = populartimes.get(api_key, ["bar", "restaurant"], bound_lower, bound_upper)
    
    df = pd.DataFrame(data)

    print(df)
    
    # with open('crowds.csv', 'wb') as file:
    #     #let w represent our file
    #     w = csv.writer(file)
        