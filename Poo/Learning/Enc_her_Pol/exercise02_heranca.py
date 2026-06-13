class funcionario:
    def __init__(self):
        self.nome = input("nome:")
        self.salario = float(input("salario:"))

    def exibir_dados(self):
        print(f"{self.nome} tem salario:{self.salario}")

class gerente(funcionario):
    def __init__(self):
        self.bonus = float(input("bonus:"))
        super().__init__()

    def exibir_dados(self):
         print(self.nome ,"tem salario:", self.salario, "e bonus:", self.bonus)

class dev(funcionario):
    def __init__(self):
        self.linguagem = input("linguagem:")
        super().__init__()

    def exibir_dados(self):
        print(self.nome, "tem salario:", self.salario ,"e ultiliza linguagem:", self.linguagem)

ger = gerente()
dev01 = dev()

for x in (ger,dev01):
    x.exibir_dados()
