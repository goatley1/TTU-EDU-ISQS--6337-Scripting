#Creator:  Aaron Oatley
#Date:  2020.06.13
#Assignment 5-2

class CellPhone:
    #initialize attributes for manufacturer, model, and price
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price
    #defin set methods to accept artuments for manufacturer, model and price.
    def set_manufact(self, manufact):
         self.__manufact = manufact
    def set_model(self,model):
        self.__model = model
    def set_retail_price(self,price):
        self.__retail_price = price
    #define get methods ro return attribute values
    def get_manufact(self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price
    def __str__(self):
        print()
        return 'You entered the following information:\n\nManufacturer:\t'+self.__manufact +'\n\n'+'Model Number:\t'+self.__model+'\n\n'+'Retail Price:\t' + '${:,.2f}'.format(self.__retail_price)
        
        
