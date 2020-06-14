#Creator:  Aaron Oatley
#Date:  2020.06.12
#Assignment 4-2

#define main function

def main():
    #declare variabl for course lookup
    course = '0'
    #declare control key
    cont = 'y'
    #define Room number dictionary
    courseRoom = {'ISQS 5347':'BA 289','ISQS 6337':'BA 015','ISQS 6349':'BA 287','ISQS 6348':'BA 021'}
    #define instructor dictionary
    courseInstructor = {'ISQS 5347':'Zadeh','ISQS 6337':'Song','ISQS 6349':'Kim','ISQS 6348':'Benjamin'}
    #define tuple for course time
    courseTime = {'ISQS 5347':'8:00 a.m.','ISQS 6337':'2:00 p.m.','ISQS 6349':'9:00 a.m.','ISQS 6348':'2:00 p.m.'}
    #define while loop control structure.
    while cont == 'y':
        #get input from user
        course = input('Please enter a course number (e.g., ISQS 1234):  ')
        #look up key for dictionaries and print results
        print('The details for your course '+course+' are:')
        print('Time:\t\t'+courseTime[course])
        print('Room:\t\t'+courseRoom[course])
        print('Instructor:\t'+courseInstructor[course])
        #get user input for loop control
        cont = input('Would you like to look up another course y/n?')
        
main()
