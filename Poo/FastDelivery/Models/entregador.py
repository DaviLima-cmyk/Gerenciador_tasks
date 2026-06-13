from Models.pessoa import Pessoa #importacao de classe

class Entregador(Pessoa): #Classe entragador herdara todos os atributos de Pessoa
    def __init__(self, nome,veiculo,cnh):
        self._nome = nome
        self._veiculo = veiculo
        self.cnh = cnh
        super().__init__(nome)

   
