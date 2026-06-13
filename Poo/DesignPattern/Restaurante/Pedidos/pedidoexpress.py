from Pedidos.strategyPedido import StrategyPedido

class PedidoExpress(StrategyPedido):
    def pedido(self, valor):
        taxa = valor * 0.8
        total = taxa + valor
        
        return total