import pyautogui as py
import time as ty


def timerzone():
    ty.sleep(3)#parametro recebe o tempo em segundos

def coordenadas():
    print(py.position())

timerzone()
coordenadas()