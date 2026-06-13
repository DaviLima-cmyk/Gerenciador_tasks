from metClassabs import Televisor

class Qled(Televisor):
    def __init__(self,img,aud):
        
        self.img = img
        self.aud = aud

    def som(self):
        return(f'O led possui audio{self.aud}')

    def imagem(self):
        return(f'O led possui imagem:{self.img}')

    def info(self):
        return(f' Imagem: {self.img} Audio: {self.aud}')
    
    
