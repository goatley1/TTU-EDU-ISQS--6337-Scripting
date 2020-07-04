#Creator:  Aaron Oatley
#Date:  2020.06.30
#Assignment 9-2

#set environment and import packages


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#load data from file

titanic = pd.read_csv('Titanic.csv')

myData = pd.DataFrame(titanic)

#drop  'PassengerID' 'Name,' ‘Ticket,’ and ‘Cabin.’ 

myData = myData.drop( ['PassengerId', 'Name', 'Ticket',  'Cabin'], axis = 1 )

print(myData.head())

#convert male and femalie to new binary definition

myData.Sex = myData.Sex.map({'female':0,'male':1})

print()
print(myData.head())


survival_counts = pd.crosstab(myData.Survived, myData.Pclass)
#Examine Survival by Pclass
survival_counts.plot.barh(stacked = True)
plt.title('Titanic Survivors by Passenger Class')
plt.xlabel('Passengers')
plt.ylabel('1 = Survived')
print() 

#Examine Survival by Sex

myData.Sex = myData.Sex.map({0:'female',1:'male'})
sex_count = pd.crosstab(myData.Survived, myData.Sex)
sex_count.plot.barh(stacked = True)
plt.title('Titanic Survivors by Passenger Sex')
plt.xlabel('Passengers')
plt.ylabel('Survived = 1')
print() 

#create boolean for survivors filter for survivors and get average age

is_Survivor = myData.Survived == 1
is_Casualty = myData.Survived == 0

df_Survivor = myData[is_Survivor]
df_Casualty = myData[is_Casualty]
print('The average survivor was age:  ',round(np.mean(df_Survivor.Age),0))
print('Survivor age standard deviation:  ',round(np.std(df_Survivor.Age),0))
print('The average casualty was age:  ',round(np.mean(df_Casualty.Age),0))
print('Casualty age standard deviation:  ',round(np.std(df_Casualty.Age),0))
print()

print('From the data we can see that survivors were on average 28 years old.  While the average age of the casualty was 31.')
print('Survivors were about twice as likely to be female as male.')
print('Further, first class passengers survived at a higher rate than second and third class.')
print('Thus, if you were going to take a trip on the titanic, your odds of survival improve greatly if you were young, female, and wealthy')


