from empregado import Empregado

class Rh (Empregado):
    def calc_bonus(self):
        return self._salario * 0.1