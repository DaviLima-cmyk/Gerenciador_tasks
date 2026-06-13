from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self,saldo,sal_pou):
        self.__sal_pou = sal_pou
        super().__init__(saldo)

    def get_saldo(self):
        return(f"Saldo Conta poupanca:{self.__sal_pou}")
        