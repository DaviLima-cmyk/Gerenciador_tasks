from abc import ABC,abstractmethod

class Veiculo(ABC):
   
   @abstractmethod
   def calc_diaria(self):
      pass
   
   @abstractmethod
   def validar_disp(self):
      pass
   
   @abstractmethod
   def info(self):
      pass
   
   @abstractmethod

   def add_veiculo(self):
      pass