from Interface.calc_frete import CalculoFreteInterface #importacao da interface de calcular frete

class EntregaComum(CalculoFreteInterface): #criacao de subclasse
    def __init__(self,distancia):
        self.distancia = distancia

    def calc_frete(self): #Metodo abstrato da Interface

        print(f'valor:{self.distancia * 1.5}')
    
class EntregaExpressa(CalculoFreteInterface): #criaçao de subclasse
    def __init__(self,distancia):
        self.distancia = distancia

    def calc_frete(self):
         print(f'valor:{self.distancia * 3}')
    
class EntregaPremium(CalculoFreteInterface): #criacao de subclasse
    def __init__(self,distancia):
        self.distancia = distancia

    def calc_frete(self):
        print(f'valor:{self.distancia * 5 + 20}')