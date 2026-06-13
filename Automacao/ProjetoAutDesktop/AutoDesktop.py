import datetime as dt
import pyautogui as pyau
import tkinter as tk

def CreateRelat():
    pyau.click(x=467, y=333)
    pyau.write("Relatorio 01\n")
    pyau.write("Data e hora local:",print(data()))



def CreateIcon(windon):
    icon = tk.Button(windon,text = "Abrir Bloco de Notas",command = OpenNotes)
    icon.pack(pady = 10)

def CreateWindow():
    windon = tk.Tk()
    windon.title("Desktop")
    windon.geometry("300x200")
    CreateIcon(windon)
    windon.mainloop()

def OpenNotes():
    pyau.press("win")
    pyau.write("Bloco de Notas")
    pyau.press("enter")

def data():
    dt.datetime.now()