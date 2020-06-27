#Creator:  Aaron Oatley
#Date:  2020.06.18
#Assignment 6-2

class Employee:
    #define init method to accept arguments
    def __init__(self, empNm, empId):
        #Initialize attributes
        self.__empNm = empNm
        self.__empId = empId
    #Define set methods
    def set_empNm(self, empNm):
        self.__empNm = empNm
    def set_empID(self, empId):
        self.__empId = empId   
    #Define get methods   
    def get_empNm(self):
        return self.__empNm
    def get_empId(self):
        return self.__empId
    
#define employee subclass production worker
class ProductionWorker(Employee):
    #define init method to accept arguments
    def __init__(self, empNm, empId, payRate, shftNbr):
        #Call the superclass __init method and pass required arguments
        Employee.__init__(self, empNm, empId)
        #Initialize s;ubclass attributes attributes
        self.__payRate = payRate
        self.__shftNbr = shftNbr
    #Define set methods or mutators
    def set_payRate(self, payRate):
        self.__payRate = payRate
    def set_shftNbr(self, shftNbr):
        self.__shftNbr = shftNbr
    #Define Get metho9ds/accessors
    def get_payRate(self):
        return self.__payRate
    def get_shftNbr(self):
        return self.__shftNbr