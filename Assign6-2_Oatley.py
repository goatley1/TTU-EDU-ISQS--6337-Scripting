#Creator:  Aaron Oatley
#Date:  2020.06.18
#Assignment 6-2


#Import class
import empOatley

#define main function

def main():
    #initialize variables
    empNm = ''
    empId = ''
    shftNbr = 0
    payRate = 0
    empNm = input('Enter your name:\t')
    empId = input('Enter your ID number:\t')
    shftNbr = int(input('Enter the shift number:\t'))
    payRate = float(input('Enter your hourly rate:\t'))
    #create the instance of the class
    employee = empOatley.ProductionWorker(empNm, empId, payRate, shftNbr)
    #print the results
    print('Production Worker Information:') #Creator:  Aaron Oatley
#Date:  2020.06.18
#Assignment 6-2
    print('Name:  ',employee.get_empNm())
    print('ID Number:  ', employee.get_empId())
    print('Shift:  ', employee.get_shftNbr())
    print('Hourly Pay Rate:  $', employee.get_payRate())
main()
    
