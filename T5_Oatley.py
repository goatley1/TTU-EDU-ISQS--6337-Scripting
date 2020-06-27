#Creator:  Aaron Oatley
#Date:  2020.06.16
#Assignment Test 2 T5

#define main function

def main():
    #declare local variables
    file_nm = 'Tnumbers.txt'
    infile = '0'
    line = 0
    mean = 0
    number = 0
    outfile = open('resultsOATLEY.txt', 'w')
    numlist = []
    #import stats for mean functgion
    import statistics as st
    #open file for reading
    infile = open(file_nm,'r')
    line = infile.readline()
    #set readline control structure
    while (line != ''):
        number = float(line)
        numlist.append(number)
        line = infile.readline()
    print(numlist)
    #calculate mean
    mean = st.mean(numlist)
    print(mean)
    #write mean to file
    outfile.write(str(mean))
    #close files
    infile.close()
    outfile.close()
main()