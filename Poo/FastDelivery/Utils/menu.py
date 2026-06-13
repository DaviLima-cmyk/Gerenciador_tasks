from Services.cliente_service import cadastrar_cliente,Listar_Clientes,buscar_cliente
from Services.entrega_service import cadastrar_entregador,listar_entregador,buscar_entregador
from Services.pedido_service import cadastrar_pedido,listar_pedidos,valor_frete,estado

print('1 - Cadastrar cliente')
print('2 - Listar Clientes')
print('3 - Procurar Cliente')
print('4 - Cadastrar Entregador')
print('5 - Listar Entregador')
print('6 - Procurar entregador')
print('7 - Criar pedido ')
print('8 - Listar Pedido')
print('9 - valor Frete')
print('10 - Status de entrega')
print('11 - sair')


def Menu():
    while True:
        op = int(input())

        if op == 1:
            cadastrar_cliente('Luis',313131,88534593535,'Rua.SaoBernardo')
        elif op == 2:
            Listar_Clientes()
        elif op == 3:
            buscar_cliente(313131)
        elif op == 4:
            cadastrar_entregador('Andre','lambreta','A')
        elif op == 5:
            listar_entregador()
        elif op == 6:
            buscar_entregador('Andre')
        elif op == 7:
            cadastrar_pedido(123,'Matheus',30,120,'comum')
        elif op == 8:
            listar_pedidos()
        elif op == 9:
            valor_frete('comum')
        elif op == 10:
            estado('entregue')
        else:
            break







