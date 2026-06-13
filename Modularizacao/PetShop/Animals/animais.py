from animal import Animal

class Dog(Animal):
    def __init__(self, name, weight,breed,size):
        self.breed = breed
        self.size = size
        super().__init__(name, weight)

    def get_show(self):
            return(f" {self.get_name()} , {self.get_weight()} and {self.bath_price()}coins,and your Breed {self.breed} your size is {self.size}")
    
class Bird(Animal):
     def __init__(self, name, weight,color):
          self.color = color
          super().__init__(name, weight)

     def get_show(self):
            return(f" {self.get_name()} ,{self.get_weight()} and price {self.bath_price()} coins,and your color is {self.color}")
     
