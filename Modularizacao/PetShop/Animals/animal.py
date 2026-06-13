class Animal:
    def __init__(self,name,weight):
        self.__name = name
        self.__weight = weight
    
    def set_weight(self,weight):
        if weight > 0 :
            self.__weight = weight

        else:
            raise ValueError("Invalid Weight")
    
    def bath_price(self):
        price = 30.00 + 2*self.__weight
        return(price)
    
    def get_name(self):
        return(f"Your pet is {self.__name}" )
    
    def get_weight(self):
        return(f"your weight is {self.__weight}")
    
    
    
    
    

