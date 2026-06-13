class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"the name of my pet is {self.name} and")
    
class Dog(Animal):
    def __init__(self,name):
        self.sound = input("pets`song:")
        super().__init__(name)


    def speak(self):
        print(f"the name of my pet is {self.name} and he does {self.sound}")

d1 = Dog("furico")
d1.speak()