import tkinter as tk
from funcoesIntAut import auto

window = tk.Tk()
window.title("JanelaAutomacao")
window.geometry("300x200")
icon = tk.Button(window,text = "Automatizar",command = auto)
icon.pack(pady = 10)

window.mainloop()