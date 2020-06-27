#Creator:  Aaron Oatley
#Date:  2020.06.16
#Assignment Test 2 part b

#define main function

def main ():
    #load statistics module to access mean function
    import statistics as st
    #declare variabls to include empty list for population.
    numlist = []
    maxn = 0
    total = 0
    minn = 0
    mean = 0
    #Declare accumulator/counter variable
    n = 1
    #Set control statement to limit input
    while n <= 10:
        #append list with user input including counter
        numlist.append(float(input('Please enter number '+str(n)+' of 10:  ')))
        n += 1
    #calculate statistics    
    total = sum(numlist)
    maxn = max(numlist)
    minn = min(numlist)
    mean = st.mean(numlist)
    #print results
    print('\nLow:\t\t',minn,'\n\nHigh:\t\t',maxn,'\n\nTotal:\t\t',total,'\n\nAverage:\t',mean)

main()    
