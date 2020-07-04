#Creator:  Aaron Oatley
#Date:  2020.07.03
#Assignment Test 4 part A

#set environment and import packages


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

stock = pd.read_csv('stock3.csv')

stock = pd.DataFrame(stock)

print(stock.head())

#plot daily price for apple google and google vs apple

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(stock.AAPL, label = 'APPLE')
plt.title('Closing Price Apple')
plt.xlabel('Day')
plt.ylabel('Price')
plt.legend()

fig2 = plt.figure()
ax1 = fig2.add_subplot(111)
ax1.plot( stock.GOOG, label = 'GOOGLE')
plt.title('Closing Price Google')
plt.xlabel('Day')
plt.ylabel('Price')
plt.legend()


fig3 = plt.figure()
ax1 = fig3.add_subplot(111)
ax1.plot( stock.GOOG, label = 'GOOGLE')
ax1.plot(stock.AAPL, label = 'APPLE')
plt.title('Closing Price Apple vs Google')
plt.xlabel('Day')
plt.ylabel('Price')
plt.legend()


#create percent daily change vectors
daily_AAPL = stock['AAPL']/stock['AAPL'].shift(1) -1
daily_GOOG = stock.GOOG/stock.GOOG.shift(1) -1
daily_CVS = stock['CVS']/stock['CVS'].shift(1) -1
daily_EBAY = stock['EBAY']/stock['EBAY'].shift(1) -1

#Density plot of rates of change

fig4 = plt.figure()
ax1 = fig4.add_subplot(111)
daily_GOOG.plot.density()
daily_AAPL.plot.density()
plt.title('Google vs Apple Percent Dail Change')
plt.xlabel('Percent Change')
plt.legend()

#Scatter plots of daily rate of google and apple

fig5 = plt.figure()
ax1 = fig5.add_subplot(111)
plt.scatter(daily_GOOG, daily_AAPL )
m, b = np.polyfit(daily_GOOG.dropna(),daily_AAPL.dropna(),1 )
plt.plot(daily_GOOG, m*daily_GOOG + b, color = 'r', label = "Regression Line")
plt.title('Change in Apple vs Google')
plt.xlabel('Google')
plt.ylabel('Apple')
plt.legend()

#calculate and visualize correlations
print()
print(stock.corr())
fig6 = plt.figure()
ax1 = fig6.add_subplot(111)
sb.heatmap(stock.corr())
plt.title('Correlation of Stock Prices')
