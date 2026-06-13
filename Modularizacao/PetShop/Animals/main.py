from animais import Dog,Bird

dog = Dog("thomas",40.0,"buldog",1.20)
bird = Bird("tails",2.0,"black")

for i in (dog,bird):
    print(i.get_show())


#Alteracao de peso para negativo

#Tratamento de erros

# atribuicao de valores Genericos negativos
try:
    dog.set_weight(-80) or bird.ser_weight(-20)
except ValueError as e:
    print("Invalid Error {NegativeWeight}")
