class ProcessaPedigo:
    def __init__(self,strategy):
        self.strategy = strategy

    def realize_pedido(self,valor):
        self.strategy.pedido(valor)