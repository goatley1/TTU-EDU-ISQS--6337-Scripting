#Creator:  Aaron Oatley
#Date:  2020.06.06
#Assignment 3-1

#Declare global constant for percentrc.

percentrc = .8


#define main function to to solicit inpuut from user and calculate the insurance amount to be passed to main function.



def main():
    rc = 0.0
    rc = float(input('Enter the replacement cost in dollars:'))
    showInsure(rc)

#define show insurance function to recieve rc and print output

def showInsure(rc):
    print('Replacement cost:  ', '${:,.2f}'.format(rc))
    print('Percent insured: ','{:.0%}'.format(percentrc))
    print('Minimum insurance:  ','${:,.2f}'.format(rc*percentrc))

main()