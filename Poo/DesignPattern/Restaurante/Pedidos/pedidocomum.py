from Pedidos.strategyPedido import StrategyPedido

class PedidoComum(StrategyPedido):
    def pedido(self, valor):
        taxa = valor * 0.5

        total = valor + taxa

        return total
    
   