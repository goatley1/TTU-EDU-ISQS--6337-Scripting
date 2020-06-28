#Creator:  Aaron Oatley
#Date:  2020.06.26
#Assignment 8-1

#set environment and import necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#define data as dictionary

dict_temps = {'CityA_High':[33,37,44,56,67,75,79,78,71,60,50,38], 
           'CityA_Low':[19,22,28,38,47,57,62,60,53,42,35,24], 
            'CityB_High':[54,59,67,76,83,91,93,94,84,75,63,55], 
            'CityB_Low':[26,30,37,46,56,65,69,67,59,48,36,28]}

#convert data to dataframe and index months of the year

df_temps = pd.DataFrame(dict_temps, index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )

#display data
print(df_temps)
print()
#create line chare and title chart and axes

df_temps.plot.line(color = ['r','b','m','g'])
plt.title('Change in High/Low Temp Over Time')
plt.xlabel('Month')
plt.ylabel('Temp in F')
print()
#create bar chart and title chart and axes
  
df_temps.plot.bar(color = ['r','b','m','g'])
plt.title('Monthly High/Low Temps for Cities A and B')
plt.xlabel('Month')
plt.ylabel('Temp in F')
print()
#plot 2 data sets in scatter chart and add lables and legend

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x =df_temps['CityA_High'], y = df_temps['CityB_High'], color = 'r', label = 'High')
ax1.scatter(x = df_temps['CityA_Low'], y = df_temps['CityB_Low'], color = 'b', label = 'Low')

plt.title('Correlation Between City A & B Temps')
plt.xlabel('Temp City A')
plt.ylabel('Temp City B')
plt.legend()

