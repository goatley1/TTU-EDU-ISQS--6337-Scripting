#Creator:  Aaron Oatley
#Date:  2020.06.13
#Assignment 5-2


#define main function
def main():
    #declare local variables
    file_nm = '0'
    infile = '0'
    line = '0'
    c = 0
    #prompt user input of the file and assign file name to var
    file_nm = input('Please enter the name of the file (e.g., filename.txt):')
    print()
    #open file and assign it to a variable
    infile = open(file_nm,'r')
    #read first line for loop test
    line = infile.readline()
    #establish control structure with & statement to give 2 stop conditions
    while (line != '') & (c != 5):
        #print current line
        print(line)
        #increas counter/accumulator
        c += 1
        #read next line
        line = infile.readline()
    #close file
    infile.close()

main()    
    