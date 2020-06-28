#Creator:  Aaron Oatley
#Date:  2020.06.27
#Assignment 8-2

#set environment and import necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#create dictionary from data

dict_pop = {'State':['CA', 'TX', 'FL', 'NY', 'IL', 'PA'], 'TimeZone':['PST', 'CST', 'EST', 'EST', 'CST', 'EST'], 
            'Population':[39250, 27862, 20612, 19745, 12801, 12784], 
            'Percentage':[12.0, 09.0, 06.0, 06.0, 04.0, 04.0]}

#create data frame and format percentageg

pd.options.display.float_format = '{0:.0f}%'.format
df_pop = pd.DataFrame(dict_pop,)

#display dataframe

print(df_pop)
print()

#Sort by TimeZone and display

df_pop = df_pop.sort_values(['TimeZone','State'])
print(df_pop)

#calculate real population and display results

df_pop['RealPopulation'] = df_pop.Population * 1000
print()
print(df_pop)

# use describe function to get min, max, and mean and display results

print()
print(df_pop.describe())

#Summarize population by time zone

grp_tz = df_pop.Population.groupby(df_pop.TimeZone)
grp_tz = grp_tz.sum()
print()
print('Population by Time Zone')
print(grp_tz)
print()

plt.title('Population by Time Zone')
plt.ylabel('In Thousands')
plt.xlabel('Time Zone')


#Draw a bar plot to show the states’ populations. The title of the plot is ‘Population,’ and the labels of Y and X axis are ‘In Thousands’ and ‘State,’ respectively.


sns.barplot(x = df_pop.State, y = df_pop.Population)
plt.title('Population by State')
plt.ylabel('In Thousands')
plt.xlabel('State')
print()
#Draw a pie plot to show the states’ populations.



fig = plt.figure()
ax3 = fig.add_subplot(111)
ax3.pie(df_pop.Population, labels = df_pop.State)
plt.title('Population by State')
