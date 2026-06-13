#ultilizado para proteger metodos e atributos de uma classe especifica.

# class Pessoa:
#     def __init__(self):
#         self.nome = input("Nome:")
#         self.__cpf = int(input("cpf:"))

# p1 = Pessoa()
# print(p1.nome)
# print(p1.cpf) #erro,pois atributo cpf esta encapsulado

#COMO OBTER ATRIBUTOS ENCAPSULADOS?


class Pessoa:
    def __init__(self):
        self.nome = input("Name:")
        self.__cpf = int(input("cpf:"))

    def get_cpf(self): #metodo que desencapsula o atributo cpf
        print(f"cpf:{self.__cpf}")

p1 = Pessoa()
p1.get_cpf()


