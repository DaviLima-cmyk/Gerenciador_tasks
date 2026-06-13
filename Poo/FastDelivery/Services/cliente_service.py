from Models.cliente import Cliente

List_Clientes = []

#Servicos de Clientes

def cadastrar_cliente(nome,cpf,telefone,endereco):
    
    c1 = Cliente(nome,cpf,telefone,endereco)
    List_Clientes.append(c1)

    print('Cliente Cadastrado')

def Listar_Clientes():
    for c in(List_Clientes):
        print(f'{c._nome} {c._cpf} {c.telefone} {c.endereco}')
    
def buscar_cliente(cpf):
    for c in (List_Clientes):
        if c._cpf == cpf:
           print('Cliente encontrado')
        else:
            print('Cliente nao encontrado')