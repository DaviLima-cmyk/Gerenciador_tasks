#arrays sao estruturas de dados mutaveis em python

# Estrutura:

#ex01:



def Mostrar():
    for game in Games:
        print(game)

def add():
    game = input("insira um jogo na coletanea:")
    Games.append(game)

def addPosicao():
    ind = int(input("digitar posicao desejada:"))
    game = input("digitar nome do jogo:")
    Games.insert(ind-1,game)
    print("Jogo adicionado ")

def RemoverGame():
    src_game = input("Jogo a ser deletado:")

    
    if src_game in Games:
        Games.remove(src_game)
        print("Jogo removido")
        
    else:
        print("Jogo nao encontrado")

def RemoverPosicao():
    index = int(input("Digitar posicao a ser removida:"))
    if(index > len(Games)):
        print("Numero ultrpassou quantidade de itens")
    else:
        Games.pop(index - 1)
        print("Jogo removido")

Games  = []

while True:
    esc = int(input("digitar escolha:"))

    if(esc == 1):
        Mostrar()

    if(esc == 2):
        i = 0
        quant = int(input("quantidade requisitada:"))
        while(i<quant):
            add()
            i+=1

    if(esc == 3):
        if(Games == []):
            print("Lista vazia,insira ao menos 1 elemento:")
        else:
            i = 0
            quant = int(input("quantidade requisitada:"))
            while(i<quant):
                addPosicao()
                i+=1

    if(esc == 4):
        if(Games == []):
            print('Nenhum jogo encontrado')
        else:
            RemoverGame()

    if(esc == 5):
        if(Games == []):
            print("Nehum jogo encontrado")
        else:
            RemoverPosicao()

    if(esc == 6):
        
        break

    

