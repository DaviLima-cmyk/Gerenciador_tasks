




try:

    caminho = r"C:\Users\Micro\OneDrive\Documentos\projetoPython\Tratamento de erros"
    file = open("davi.txt","r")
    if file not in (caminho):
        raise FileNotFoundError('Arquivo nao encontrado')
    
except FileNotFoundError as e:
    print (f"Erro de Caminho",{e})

finally:
    print(f"Programa Finalizado")
