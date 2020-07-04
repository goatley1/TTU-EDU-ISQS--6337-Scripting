#Creator:  Aaron Oatley
#Date:  2020.07.03
#Assignment Test 4 part B

#set environment and import packages


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import statsmodels.api as sm


#load data and create data frame

avcd = pd.read_csv('avocado.csv')

avcd = pd.DataFrame(avcd)
print(avcd.head())

#Scatter plot of volume and avg price # log 10 of volume because of the spread of the data
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
plt.scatter(avcd.AveragePrice, avcd['Total Volume'] )
plt.title('Avocados: Average Price vs. Total Volume')
plt.xlabel('Average Price')
plt.ylabel('Volume')
plt.legend()


#scatter plot of price vs total bags


fig2 = plt.figure()
ax1 = fig2.add_subplot(111)
plt.scatter(avcd.AveragePrice, avcd['Total Bags'] )
plt.title('Avocados:  Average Price vs. Total Bags')
plt.xlabel('Average Price')
plt.ylabel('Bags')
plt.legend()

print('At first glance these relationships look Negative.')

print(avcd.corr())

#create simple OLS linear model convert categorical to boolean

avcd.type = avcd.type.map({'conventional':0,'organic':1})

y = avcd[['AveragePrice']]
x = avcd[['Total Volume', 'Total Bags', 'type', 'year']]
model = sm.OLS(y,x).fit()

print(model.summary())

print('According to our summary, these 4 variables explain about 95% of the variation in our avocado price.')
print('We can see that type and year have positive correlation based on our coeficient.  This means that as time goes buy the price goes up.  Avocados are more expensive now then they were a few years ago.  Also oranics are more expensive than conventional.  Volume which has a direct relation to bags both have negative relationships to price.  As the number of bags and avocados slold increase the price decreases.')

