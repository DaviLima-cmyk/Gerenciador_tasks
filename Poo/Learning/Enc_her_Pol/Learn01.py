# Ultilizada em grandes projetos,porque pode ser reultilizado em projetos maiores e tambem e mais facul de realizar manuntençoes


# Classe -> molde de onde surgem os objetos

# Objetos - > elementos pertencentes a classe,tambem chamados de instancias quando referidos a uma classe em especifica

# atributos -> caracteristicas atribuidas as instancias


class Pessoa:
     def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

     def saudacao(self):
        print(f"ola meu nome é {self.nome} ,tenho {self.idade} anos e tenho cpf:{self.cpf}")
        


p1 = Pessoa("Alan",23,124121345353)
p1.saudacao()

# deletar objetos:

# del p1


