#ultilizado em classes para com o intuito de atribuir metodos ou atributos para objetos semelhantes entre classes distintas ,com saidas diferentes

class cat:
    def __init__(self):
        self.nome = input("cat`s name:")
    def sound(self):
        print(f"{self.nome} faz miau")

class fox:
    def __init__(self):
        self.name = input("fox`s name:")
    def sound(self):
        print(f"{self.name} faz tututu")

cat01 = cat()
fox01 = fox()

for i in (cat01,fox01):
    i.sound()