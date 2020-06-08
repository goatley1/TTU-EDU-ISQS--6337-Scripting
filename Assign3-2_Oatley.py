#Creator:  Aaron Oatley
#Date:  2020.06.06
#Assignment 3-2

#Declare global constant for tax rate and assessment.

asc_perc = .6
tax_rate = 0.0072

#define main function to to solicit inpuut from user and calculate assessed value and tax amount



def main():
    pv = 0
    asc_val = 0
    prop_tax = 0
    pv = float(input('Enter the property value in dollars:'))
    asc_val = pv*asc_perc
    prop_tax = asc_val*tax_rate
    showPropertyTax(asc_val,prop_tax)

#define show prop tax...print and format assessed value and tax amount
def showPropertyTax(asc_val,prop_tax):
    print('Assessed value:', '${:,.2f}'.format(asc_val))
    print('Property Tax: ','${:,.2f}'.format(prop_tax))

main()