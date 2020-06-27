#Creator:  Aaron Oatley
#Date:  2020.06.24
#Assignment Test 3 Part B

#Declare the class

class RetailItem:
    #initialize attributes for price units, and destiption
    def __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price
    #define set methods to mutate desc, units and price
    def set__desc(self, desc):
        self.__desc = desc
    def set__units(self, units):
        self.__units = units
    def set__price(self, price):
        self.__price = price
    #define get methods to access desc, units and price   
    def get__desc(self):
        self.__desc = desc    
    def get__units(self):
        self.__units = units
    def get__price(self):
        self.__price = price
    def __str__(self):
        return 'Description:\t'+self.__desc +'\nUnits in Inventory:\t' + str(self.__units)+'\nPrice: $' + str(self.__price)
        print() 