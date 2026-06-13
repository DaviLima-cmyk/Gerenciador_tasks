from metClassabs import Televisor

class Led(Televisor):
    def __init__(self,comprimento,largura,img,aud):
        self.comprimento = comprimento
        self.largura = largura
        self.img = img
        self.aud = aud


    

    def som(self):
        return(f'O led possui audio{self.aud}')

    def imagem(self):
        return(f'O led possui imagem:{self.img}')

    def info(self):
        return(f'Comprimento {self.comprimento} Largura: {self.largura} Imagem: {self.img} Audio: {self.aud}')
    

