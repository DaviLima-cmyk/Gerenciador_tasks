import os
import time #biblioteca de temporizador


def timerzone():
    time.sleep(1) #parametro recebe o tempo em segundos


if not os.path.exists("Backup"): #criacao de diretorio(pasta)
    os.mkdir("Backup")
    print("Criada")
else:
    print("A pasta ja existe")

way = "C:/Users/Micro/OneDrive/Documentos/projetoPython/Automacao" #obs:usar getcwd seria mais viavel(obter pasta atual)

arquives = os.listdir(way) #listar arquivos

for arquive in arquives:
    timerzone() #demorar um segundo para chamar cada arquivo
    
    print(arquive)