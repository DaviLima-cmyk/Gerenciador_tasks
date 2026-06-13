class pai: #Criacao da classe pai
    def __init__(self,nome,sobrenome):#atribuicao de met.construtor (atribudos em comum para todos os objetos criados a partir dessa classe)
        self.nome = nome
        self.sobrenome = sobrenome

    def apresentacao(self): #metodo em comum para todos os objetos criados a partit dessa classe
        print(f"ola,me chamo {self.nome} e tenho sobrenome {self.sobrenome}")


class filho(pai): #criacao da classe filha,esta herdara metodos e atributos da classe pai
    def __init__(self,nome,sobrenome): 

        self.idade = int(input("idade:"))#atributo pertencente especificadamente apenas a classe filho

        pai.__init__(self,nome,sobrenome) #garante a preservacao dos atributos da classe pai -->#obs:usar "super().",ao inves do nome da classe do pai,tambem preservara
        #os atributos e metodos de tal classe.
        
    def apresentacao(self):
        print(f"me chamo {self.nome} e tenho sobrenome {self.sobrenome} e idade {self.idade}")
        
    
        


x = filho("mula","sem cabeca") #criacao do objeto oriundo de filho com todos os metodos do pai
x.apresentacao() #chamada do metodo

