# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def show(self):
#         print(f"Marca:{self.brand}")

# car1 = Car("Fiat")
# car1.show()


# RETANGULO


class Retangular:
    def __init__(self,widht,height):
        self.widht = widht
        self.height  = height

    def area(self):
        area = self.widht * self.height
        return area
    
ret1 = Retangular (23,2)
print(ret1.area())