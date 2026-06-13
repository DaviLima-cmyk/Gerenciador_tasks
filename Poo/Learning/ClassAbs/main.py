from led import Led
from qLed import Qled

led01 = Led(80,50,'HD','HDMI')

qled01 = Qled('4K','Interno')


for item in (led01,qled01):
    print(item.info())