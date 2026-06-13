from empregado import Empregado

class Dev (Empregado):
    def calc_bonus(self):
        return self._salario *0.3