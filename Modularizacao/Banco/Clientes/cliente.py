
class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.contas = []

    def adicionar_conta(self,conta):
        self.contas.append(conta)
   
    

class Pessoa(Cliente):
    def __init__(self, nome,cpf,numero):
        self.__cpf = cpf
        self.numero = numero
        super().__init__(nome)

    def set_cpf(self,cpf):
        if cpf < 0:
            return("cpf invalido")
        else:
            self.__cpf = cpf

        