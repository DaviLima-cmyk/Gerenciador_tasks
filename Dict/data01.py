from tkinter import messagebox

Alunos = {}



def read():
    name = input("digitar nome de aluno:")
    old = int(input("digitar idade de usuario:"))

    return name,old



def Add(name,old):
    name,old = read()
    Alunos[name] = old
    messagebox.showinfo("aluno Cadastrado")

    

def vews():
    for name,old in Alunos.items():
        print(f"{name} - {old} anos ")

        

def delete():
    src = input("digitar nome para ser excluido:")
    if src in Alunos:
        del Alunos[src]

    else:
        pass

def update():
    src = input("nome a ser atualizado:")
    if src in Alunos:
        new_name = input("digite um novo nome:")
        new_old = int(input("digite uma nova idade:"))

        del Alunos[src]

        Alunos[src] = new_name,new_old
        
    else:
        pass
    
        






