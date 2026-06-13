from abc import ABC,abstractmethod

class Empregado(ABC): #criacao de uma classe abstrata ,servira como "forma"  para subclasses
    def __init__(self,nome,salario):
        self._nome = nome
        self._salario = salario

    def get_nome(self):
        return (f"Nome:{self._nome}")
    
    def set_nome(self,nome):
        self._nome = nome

    def get_salario(self):
        return(f"Salario:{self._salario}")
    
    def set_salario(self,salario):
        if salario < 0:
            raise ValueError("Salario invalido") # tratamento de erros
        else:
            self._salario = salario
        
    def get_dados(self):
        return(f"{self.get_nome()} e {self.get_salario()}")
        
    @abstractmethod
    def calc_bonus(self):
        pass
        

