from Pedidos.strategyPedido import StrategyPedido

class PedidoPremium(StrategyPedido):
    def pedido(self, valor):
        taxa = valor * 1.5
        total = taxa + valor
        
        return total