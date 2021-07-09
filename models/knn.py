#!/usr/bin/env python
# coding: utf-8

# # Linear Regression
# 
# Here, we have some deals data for various restaurants and bars in Philadelphia area.
# 
# The individual bar/restaurant are trying to decide the deals to put forth to restaurant based on crowd level.
# 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import REGRESSION
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier


# ## Get the Data
# 
# Get the price csv file from the company. It has deal and price info.
# 

restaurant = pd.read_csv("DATASET1.csv")

# restaurant.head()

# restaurant.describe()

# restaurant.info()

# ## Data Analysis
# 
# Explore data


# More time on restaurant, more money spent.
sns.jointplot(x='CrowdSize',y='Monthly Sales',data=restaurant)

sns.jointplot(x='Deal Percent',y='Monthly Sales',data=restaurant)

sns.jointplot(x='Deal Percent',y='CrowdSize',kind='hex',data=restaurant)

sns.pairplot(restaurant)

# Length of Deal 

# linear model plot of  Monthly Sales vs. Length of Deal.

sns.lmplot(x='Length of Deal',y='Monthly Sales',data=restaurant)

# ## Training and Testing Data
# 
# Split the data into training and testing sets.
# ** Set a variable X equal to the numerical features of the restaurant and a variable y equal to the "Monthly Sales" column. **

Y = restaurant['Monthly Sales']

X = restaurant[['Deal Percent','Avg. Sales Per Hr', 'Length of Deal', 'CrowdSize']]

from sklearn import preprocessing
from sklearn import utils


from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4, random_state=4)

lab_enc = preprocessing.LabelEncoder()
x_train = lab_enc.fit_transform(x_train)
y_train= lab_enc.fit_transform(y_train)
x_test = lab_enc.fit_transform(x_test)
y_test= lab_enc.fit_transform(y_test)

print(x_train.shape)
print(x_test.shape)

print(y_train.shape)
print( y_test.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print( metrics.accuracy_score(y_test, y_pred))

k_range = range(1,26)
data = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    data.append(metrics.accuracy_score(y_test, y_pred))

print(data)
