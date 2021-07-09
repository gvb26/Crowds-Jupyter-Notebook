import pandas as pd
import numpy as np

df1 = pd.read_csv("DATASET1.csv")
sLength = len(df1['Menu Item'])
df1 = df1.assign(CrowdSize=np.random.randint(15, 100, size=sLength))
df1[['Avg. Sales Per Hr', 'Target Sales Per Hr']] = df1[['Target Sales Per Hr', 'Avg. Sales Per Hr']]
df1 = df1.assign(DealCount=np.random.randint(20, 40, size=sLength))
print(df1)

df1.to_csv("SUNDAY.csv", index=False)
