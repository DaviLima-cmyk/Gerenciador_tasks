from Clientes.cliente import Pessoa
from Operacoes.operacao import set_depositar,set_valorSaque,get_saldo,mostrar_historico 




while True:
    op = int(input("Digite de 1 a 6:"))

    if op == 1:
     c1 = Pessoa("ze",700,430)

    if op == 2:
        set_valorSaque(100)

    if op == 3:
        set_depositar(10)

    if op == 4:
        get_saldo()

    if op == 5:
        mostrar_historico(c1)

    else:
        print("Encerrado")






   