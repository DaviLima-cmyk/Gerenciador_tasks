#importacao de classe

class Pedido:
    def __init__(self,codigo,nome,peso,entrega):
        self._codigo = codigo
        self._nome = nome
        self.peso = peso
        self.entrega = entrega
        self.status = 'pendente'
        

    def calc_frete(self):
        print(f'{self.entrega.calcular_frete()}')