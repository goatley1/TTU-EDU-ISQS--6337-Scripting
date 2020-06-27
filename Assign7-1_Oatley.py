#Creator:  Aaron Oatley
#Date: 2020.06.21
#Assignment: 7-1  

#Import necessary packages

import numpy as np
import pandas as pd


#Create dictionnary

emp_dict = {'Department':['Accounting','Accounting','Sales','Sales','Sales','Sales'], 'Employee':['Margaret','Chris','Jaeki','Yuane','Nina','Lara'],'Salary':[120000,87000,43500,60000,55000,73000]}

#pass dictionary to data frame to create data frame

df = pd.DataFrame(emp_dict)

print(df)
print('\n')
#decribe the data and display results
print('This data set provides the names, positions, and salaries for employees.\nIt has the following characteristics:\n')
print(pd.DataFrame.describe(df))

#sort by departement and sort the data and print results

df_sort = pd.DataFrame.sort_values(df,by=['Department','Salary'])
print('\n')
print(df_sort)

#declare list for append

Salary_Cat = []

#Set control loop for categorization of salaries and append values

for i in df['Salary']:
    if i > 60000:
        Salary_Cat.append('high')
    elif i > 50000:
        Salary_Cat.append('medium')
    else:
        Salary_Cat.append('low')
#Add categorization to dataframe and print results   
df['Salary_Cat'] = Salary_Cat
print('\n')
print(df)   

#declare variables for mean calculation
Accounting_Mean = 0
Sales_Mean = 0
#calculate means and print results
Accounting_Mean = df[df['Department'] == 'Accounting'].Salary.mean()
Sales_Mean = df[df['Department'] == 'Sales'].Salary.mean()
print('\nThe mean salary in Accounting is:  ', Accounting_Mean)
print('\nThe mean salary in Sales is:', Sales_Mean) 
