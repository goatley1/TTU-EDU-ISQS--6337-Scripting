#Creator:  Aaron Oatley
#Date:  2020.06.13
#Assignment 5-1


#define main function 
def main():
    #declare local variables for execution
    infile = 'o'
    file_contents = '0'
    #assign .txt file to var and open file for reading
    infile = open('numbers.txt','r')
    #assing contents to variable
    file_contents = infile.read()
    #Close the file
    infile.close() 
    #print the loical variable
    print(file_contents) 
    
#call function for execution
main()

    
