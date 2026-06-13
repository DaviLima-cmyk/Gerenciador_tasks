from dev import Dev
from rh import Rh


dev01 = Dev("framco",600.0)
rh01 = Rh("Rita",900.0)


for empregado in (dev01,rh01):
    print(empregado.calc_bonus())
    print(empregado.get_dados())