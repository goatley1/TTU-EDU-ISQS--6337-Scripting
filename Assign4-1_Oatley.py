#Creator:  Aaron Oatley
#Date:  2020.06.12
#Assignment 4-1

#define the main and declare local variables/lists initialize dailey_sales, sales, n counter, and populate dow

def main():
    daily_sales = []
    dow = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Firday','Saturday']
    #initialize counter for indexing and sales var
    sales = 0
    n = 0
    #initialize control loop for sales input
    for d in dow:
        #get sales from the user
        sales = float(input('Enter the sales for '+dow[n]+':'))
        #append user entries to the sales list 
        daily_sales.append(sales)
        n += 1
    #print the total weekly sales
    print()
    print('The total sales this week = $',sum(daily_sales))
    
main()