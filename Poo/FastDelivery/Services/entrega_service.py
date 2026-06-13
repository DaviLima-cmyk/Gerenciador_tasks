from Models.entregador import Entregador

list_ent = []

#Servicos de entregadores

def cadastrar_entregador(nome,veiculo,cnh):
    ent = Entregador(nome,veiculo,cnh)

    list_ent.append(ent)
    print('Cadastrado')

def listar_entregador():
    for e in(list_ent):
        print(f'{e._nome} {e._veiculo} {e.cnh}')

def buscar_entregador(nome):
    for e in (list_ent):
        if e._nome == nome:
           print('Encontrado')
        else:
            print('Nao encontrado')