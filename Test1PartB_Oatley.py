#Creator:  Aaron Oatley
#Date:  2020.06.09
#Assignment Test1B

#This section defines the main function, declares variables and accepts user input to populate variables

def main():
    lp = 0
    ins = 0
    gas = 0
    oil = 0
    tir = 0
    maint = 0
    lp = float(input('Enter your loan payment:'))
    ins = float(input('Enter you insurance payment:'))
    gas = float(input('Enter your monthly gas expense:'))
    oil = float(input('Enter your monthly oil expense:'))
    tir = float(input('Enter your monthly tire expense:'))
    maint = float(input('Enter your monthly maintenance expense:'))
    totexp(lp, ins, gas, oil, tir, maint)

#This section defines the total expense function that acccepts arguments from the main and calcualtes 
#monthly and annual total expenses.

def totexp(lp, ins, gas, oil, tir, maint):
    totmon = lp + ins + gas + oil + tir +maint
    totan = totmon*12
    print('Total monthly expense:', '${:,.2f}'.format(totmon))
    print('Total annual expense:', '${:,.2f}'.format(totan))
    
main()
