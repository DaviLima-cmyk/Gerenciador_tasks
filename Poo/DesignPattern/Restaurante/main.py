from Pedidos.pedidocomum import PedidoComum
from Pedidos.pedidoexpress import PedidoExpress
from Pedidos.pedidopremium import PedidoPremium
from Context.processarpedido import ProcessaPedigo

p1 = PedidoComum()
process = ProcessaPedigo(PedidoComum)
process.realize_pedido(100)

p2 = PedidoExpress()
process = ProcessaPedigo(PedidoExpress)
process.realize_pedido(100)

p3 = PedidoPremium()
process = ProcessaPedigo(PedidoPremium)
process.realize_pedido(100)