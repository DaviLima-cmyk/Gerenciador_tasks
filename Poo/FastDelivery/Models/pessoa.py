from abc import ABC,abstractmethod

class Pessoa(ABC):
    def __init__(self,nome):
        self._nome = nome

        @property

        def nome(self):
            print(f'{self._nome}')
        
        @nome.setter

        def nome(self,valor):
             if any(c.isdigit() for c in valor):
                print('erro,tem um numer no nome ')
             else:
                 self._nome = valor

      
            
        


