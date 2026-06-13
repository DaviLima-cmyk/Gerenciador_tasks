from Models.pedido import Pedido
from Models.entrega import EntregaComum,EntregaExpressa,EntregaPremium
list_pedidos = []

#Servicos de Pedidos

def cadastrar_pedido(codigo,nome,peso,distancia,tip_entrega):

    if tip_entrega == 'comum':
        entrega = EntregaComum(distancia)

    elif tip_entrega == 'expressa':
        entrega = EntregaExpressa(distancia)

    else:
        entrega = EntregaPremium(distancia)


    p1 = Pedido(codigo,nome,peso,entrega)

    
    list_pedidos.append(p1)
    print('cadastrado')


def listar_pedidos():
    for p in (list_pedidos):
        print(f'{p._codigo} {p._nome} {p.peso} {p.entrega}' )

def valor_frete(entrega):
    print(entrega)

def estado(status):
    print(status)