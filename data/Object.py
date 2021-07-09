import pandas as pd

class Business:       
    def __init__(self, name, id, address, populartimes, ratings):
        self.name = name
        self.id = id
        self.ratings = ratings
        self.address = address
        self.crowdsize = populartimes

    def getAllCrowdSize(self, day):
        df = pd.DataFrame.from_dict(self.populartimes)
        df2 = df[df['name'] == day]
        return df2['data'][0]

    def getCrowdSizeByHour(self, day, hour):
        df = pd.DataFrame.from_dict(self.populartimes)
        df2 = df[df['name'] == day]
        values = df2['data'][0]
        try:
            print(values[hour])
        except ValueError:
            print("Enter right time format: 0-23")
        



