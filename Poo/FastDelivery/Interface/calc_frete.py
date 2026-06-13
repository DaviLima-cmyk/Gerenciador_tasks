from abc import ABC,abstractmethod # importacao de modulo abstrato

class CalculoFreteInterface (ABC):
    @abstractmethod # ultilizacao de metodo abstrado,sera comum a todas a subclasses que a tiverem

    def calc_frete(self):
        pass