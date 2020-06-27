#Creator:  Aaron Oatley
#Date: 2020.06.21
#Assignment: 7-2  

#Import necessary packages

import numpy as np
import pandas as pd

#Create assigned list and dictionary

id = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]

student = {'Name':['Yuan', 'David', 'Margaret', 'Daniel', 'Gina', 'Catherine', 'Chris', 'Jaeki', 'Ethan', 'Mruphy'],
           'Score':[12.5,9,16.5,'N/A',9,20,14.5,'N/A',8,19],
           'Attempt':[1,3,2,3,2,3,1,1,2,1],
           'Pass/fail':['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes']}


#Create Data Frame

df = pd.DataFrame(student, index = id)
print(df)
print('\n')
#display attempts greater than 2, score of N/A and both

print(df[df.Attempt > 2])
print('\n')
print(df[df.Score == 'N/A'])
print('\n')
print(df[(df.Score== 'N/A') & (df.Attempt > 2)])

#add index 'k'

df.loc['k']=['Song',15.5, 1,'Yes']

print(df)

#drop index h

df = df.drop(['h'])


print('\n')
print(df)

#replace no with fail and yes with pass

df = df.replace('Yes','Pass')
df = df.replace('No','Fail')

print('\n')
print(df)
