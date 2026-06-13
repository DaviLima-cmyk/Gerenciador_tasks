class Func:
    def __init__(self,nome,salbase):
        self.__nome = nome
        self.__salbase = salbase

    def set_salario(self,salbase):
        if salbase > 0:
            self.__salbase = salbase
        else:
            raise ValueError("erro,salario negativo")
        
    def get_salario(self):
        return(self.__salbase)
    
    def get_nome(self):
        return(self.__nome)
    

class Dev(Func):
    def __init__(self,bonus,nome,salbase):
        self.__bonus = bonus
        super(). __init__(nome,salbase)

    def set_bonus(self,bonus):
        if bonus > 0:
            self.__bonus = bonus
        else:
            raise ValueError("Bonus invalido")

    def get_calc(self):
        return(f"salario Final: {self.get_nome(),self.get_salario() + self.__bonus}")
    
class Gerent(Func):
    def __init__(self,part,nome,salbase):
        self.__part = part
        super(). __init__(nome,salbase)

    def set_part(self,part):
        if part> 0:
            self.__part = part
        else:
            raise ValueError("participacao invalida")
        
    def get_calc(self):
        return(f"salario final: {self.get_nome() ,self.get_salario() + self.__part}")
    

    
dev01 = Dev(-500,"alan",2000)
ger01 = Gerent(200,"yuri",6000)

for i in(dev01,ger01):
    print(i.get_calc())

       
