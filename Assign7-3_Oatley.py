#Creator:  Aaron Oatley
#Date: 2020.06.21
#Assignment: 7-3

#Import necessary packages

import numpy as np
import pandas as pd


#Import the “Athlete.csv” file in 

athlete = pd.read_csv('Athlete.csv')

#Create a data frame for the data object

df = pd.DataFrame(athlete)

print(df)

print(df.describe())



#Create a NumPy array for the data. Show how many rows and columns there are in the data. 

dfarray = np.array(df)

print(np.shape(dfarray))

#Overwrite the Year value of the 2nd row (that is, the athlete whose ID is 1) with 1993. 
#Display only the Year column to check if the value has been successfully changed.

df['Year'][0]=1993

print(df.Year)

#Deduct 10 from all athletes’ weights and show results.

df.Weight = df.Weight - 10
print(df.Weight)

#Add a new column to the array to show the ratio of weight to the height of each athlete.

df['W/H Ratio'] = df.Weight /df.Height



