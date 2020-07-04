#Creator:  Aaron Oatley
#Date:  2020.06.29
#Assignment 9-1

#set environment and import packages


import matplotlib.pyplot as plt
import pandas as pd



#load data and create data frame
dict_sal = {'Year':['2002', '2002', '2003', '2003', '2004', '2004', '2005', '2005'], 
            'Name':['Tom', 'Joe', 'Tom', 'Joe', 'Tom', 'Joe', 'Tom', 'Joe',],
            'Salary':[54000, 50000, 56000, 50000, 58120, 57100, 58120, 60300],
            'Interest_Rate':[0.10, 0.10, 0.15, 0.10, 0.16, 0.16, 0.16, 0.2]}

df_sal = pd.DataFrame(dict_sal)

#print head first 6 rows

print(df_sal.head(6))
print()
#sort data by year

df_sal = df_sal.sort_values('Year')

print(df_sal)
print()
#describe data

print(df_sal.describe())
print()
#Add Holding column

df_sal['Holding'] = df_sal.Salary * df_sal.Interest_Rate + 1500

print(df_sal)
print()
#calculate the sum of Holding for each person (i.e., Tom and Joe) over the 4 years

print(df_sal.groupby('Name')['Holding'].sum())
print()

#Draw a line plot that shows each person’s holdings change over the 4 years

grouped = df_sal.groupby(df_sal.Name)
Tom = grouped.get_group('Tom')
Joe = grouped.get_group('Joe')
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(Joe.Year, Joe.Holding, label = 'Joe')
ax1.plot(Tom.Year, Tom.Holding, label = 'Tom')
plt.title('Holding Comparison')
plt.xlabel('Year')
plt.ylabel('Holding')
plt.legend()


##endfile