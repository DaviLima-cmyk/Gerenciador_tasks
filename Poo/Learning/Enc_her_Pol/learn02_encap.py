class Personal:
    def __init__(self):
        self.nome = input("Name:")
        self.__password = input("password:") #atributo privado

    def update(self):
        new_password = input("New_password:")
        if (self.new_password!=self.__password):
            self.__password = new_password
            print()
        else:
            print("digitar senha diferente")

p1 = Personal()
p1.update()