#Creator:  Aaron Oatley
#Date:  2020.06.13
#Assignment 6-1

#import cellphone class

import cellOATLEY as cp

#define main

def main():
    #prompt user for cellphone manufacturer, model, and price
    cont = 'y'
    #use while loop so multiple phones can be entered at user request
    while cont =='y':
        manufact = input('Enter the phone manufactur:  ')
        model = input('Enter the phone model:  ')
        price = float(input('Enter the phone\'s retail price:  '))
        #create the instance of the CellPhone class
        cell = cp.CellPhone(manufact, model, price)
        print(cell)
        cont = input('Would you like to enter another phone (y/n)?')
main()  
    
    
    
    

