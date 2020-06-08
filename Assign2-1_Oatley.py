#Creator:  Aaron Oatley
#Date:  2020.06.03
#Assignment 2-1

#This section defines the variables and prompts user input of the variables. WE initialize
  #BMI as a global variable to exist outside defined functions

Height = float(input('Enter your height in inches:'))
Weight = float(input('Enter your weight in pounds:'))
BMI = 0

#The following program calculates the BMI given user inputs of weight and height.
#This section defines the function for body mass and it's outputs

def fun(Weight, Height):
    BMI = round(Weight*703/Height**2,2)
    print('\nYour Body Mass Indicator (BMI) is',BMI,'.\nOptimal BMI is between 18.5 and 25.') 
    if BMI < 18.5:
        print('You are underweight.  \nYou should increase your daily calorie intake.')
    elif BMI > 25:
        print('You are overweight.  \nYou should decrease your daily colorie intake.')
    else:
        print('Your weight is optimal.  Keep up the good work.')
         

#Run defined function
fun(Weight, Height) 
   
