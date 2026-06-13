from Contas.conta import Conta

class ContaCorrente (Conta):
    def __init__(self, saldo,sal_cor):
        self.__sal_cor = sal_cor
        super().__init__(saldo)

    def get_saldo(self):
        return(f"Saldo Conta Corrente:{self.__sal_cor}")