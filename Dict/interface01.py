import tkinter as tk #chamar biblioteca de criacao de interface janela
import data01 #chanar arquivo das funcoes




def Cadastrar(): #funcao cadastrar recebe funcao de adicionar nome e idade de data01.py
    name = entry_name.get()
    old = entry_old.get()

    data01.Add(name,old)
    
    

def Vews():
    data01.vews()

def Delete():
    data01.delete()

def Update():
    data01.update()

windon = tk.Tk() #funcao que cria a janela
windon.title("Cadastro") #atribuir nome da janela
windon.geometry("220x400") #proporcoes da janela

div = tk.Frame (padx = 8,pady= 8) #criacao de grid
div.pack()

tk.Label(div,text="NomeAluno:").grid(row = 0,column = 0,sticky = "e")
entry_name = tk.Entry(div)
entry_name.grid(row = 0,column = 1,pady = 6)


tk.Label(div,text="Idade").grid(row = 1,column = 0,sticky = "e")
entry_old = tk.Entry(div)
entry_old.grid(row = 1,column = 1,pady = 6)

#Criacao de botoes

tk.Button(div,text = "Cadastrar",command=  Cadastrar).grid(row = 2,column = 0,pady = 6,sticky = "we",padx = 5)
tk.Button(div,text = "vews",command=  Vews).grid(row = 2,column = 1,pady = 6,sticky = "we")
tk.Button(div,text = "Deletar",command =  Delete).grid(row = 3,column = 0,pady = 6,sticky = "we",padx = 5)
tk.Button(div,text = "update",command =  Update).grid(row = 3,column = 1,pady = 6,sticky = "we")


windon.mainloop()






