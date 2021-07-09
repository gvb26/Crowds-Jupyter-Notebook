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

y = restaurant['Monthly Sales']

X = restaurant[['Deal Percent','Avg. Sales Per Hr', 'Length of Deal', 'CrowdSize']]

# ** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101**

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# ## Training the Model
# 
# Train our model on our training data!
# 
# ** Import LinearRegression

# **Create an instance of a LinearRegression() model named lm.**

lm = REGRESSION.LinearRegression()

# ** Train/fit lm on the training data.**

lm.fit(X_train,y_train)

# **Print out the coefficients of the model**

# The coefficients
print('Coefficients: \n', lm.coef_)

# ## Predicting Test Data
# Now that we have fit our model, let's evaluate its performance by predicting off the test values!
# 
# ** Use lm.predict() to predict off the X_test set of the data.**

predictions = lm.predict( X_test)

# ** Create a scatterplot of the real test values versus the predicted values. **

plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')

# ## Evaluating the Model
# 
# Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).

# calculate these metrics by hand!
from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# ## Residuals
# 
# **Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().**

sns.distplot((y_test-predictions),bins=50)

# 
# Check predictions
# 
# 

coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']

#Check predicted adjustment to current Deal Percent for our test data

coeffecients.loc[['Deal Percent']]

#Check predicted Sales for Menu Item 1

print(predictions[0])

#Check predicted adjustment to crowdSize for current test data

(coeffecients.loc[['CrowdSize']]*100).apply(np.ceil)

