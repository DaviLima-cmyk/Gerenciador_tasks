


class Player():
    def __init__(self,name,choose):
        self._name = name
        self._choose = choose

    @property

    def name(self):
        return(f"{self._name}")
    
    @name.setter

    def name(self,instance):
        try:
            for key in  instance:
                if key not in['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                    raise ValueError('Invalid Name')
        except ValueError as e:
            print(f"Nome invalido ,{e}")
        else:
            self._name = instance
        finally:
            print('Tentativa de atualizar nome Concluida')

    @property

    def choose(self):
        return(f'{self._choose}')
    

    @choose.setter

    def choose(self,value):
        try:
            if value not in ['rock','scissor','paper']:
                raise ValueError('Invalid Input')
        except ValueError as e:
            print(f"Invalid value,verify your input {e}")

        else:
            self._choose = value
        finally:
            print("Value update realized")

    def evaluate(self,name01,name02):
            if name01._choose == 'rock' and name02._choose == 'rock':
                return('draw')

    def get_info(self):
        return(f'{self._nome}:{self._choose}')

p1 = Player('Vagner','rock')
p2 = Player('Robson','rock')

for p in (p1,p2):
    print(p.evaluate('Vagner','Robson'))
