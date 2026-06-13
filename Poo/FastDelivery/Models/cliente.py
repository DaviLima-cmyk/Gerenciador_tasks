from Models.pessoa import Pessoa


class Cliente(Pessoa): #criacao da classe cliente,herdara atributos de pessoa
    def __init__(self, nome,cpf,telefone,endereco):
        self._cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        super().__init__(nome) # metodo de conservacao de atributos
    