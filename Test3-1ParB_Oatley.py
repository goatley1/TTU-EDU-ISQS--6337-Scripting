#Creator:  Aaron Oatley
#Date:  2020.06.24
#Assignment Test 3 Part B


#import retail class and packages

import retailOATLEY as ro
import pandas as pd
import numpy as np


#define main function
def main():
    #create dictionary
    id = ['Product 1', 'Product 2','Product 3']
    prod_dict = {'Description':['Jacket','Designer Jeans','Shirt'],'Units':[12,30,45],'Price':[249.99, 199.99, 49.99]}
    #create data frame from dictionary
    df = pd.DataFrame(prod_dict, index = id)
    print(df)
    count = 0
    for row in df:
        desc = df['Description'][count]
        units = df['Units'][count]
        price = df['Price'][count]
        retail = ro.RetailItem(desc, units, price)
        print(df.index[count])
        print(retail)
        print()
        count+=1
        
main()    
