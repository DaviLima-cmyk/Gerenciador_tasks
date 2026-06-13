from Contas.contaCorrente import ContaCorrente
def set_valorSaque(self,valor):
      if valor <= 0 or valor > self.__saldo:
          return("Saque invalido") 

      else:
          self.valor = valor
          sal_cor -= valor
          return(sal_cor)

def get_saldo(self):
      print(f"{self.__saldo}")
      
          

def depositar(self,valor):
      self.__valor = valor


def set_depositar(self,valor):
      if valor <= 0:
            return ("valor de deposito invalido")
      else:
            self.__valor = valor
            sal_cor+= valor
            return(sal_cor)

def __init__(self):
      self.transacoes = []

def registrar_historico(self,conta,tipo,valor): #estrutura de dicionario
      conta.transacoes.append({
      "1": tipo,
      "2":valor
      }
      )

def mostrar_historico(conta):
      for h in conta.transacoes:
            return(f"{h["tipo"]} {h["valor"]}")
            
