from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,marca,quant_car,placa,ano,quant_dia):
        self.marca = marca
        self.quant_car = quant_car
        self.quant_dia = quant_dia
        self.placa = placa
        self.ano = ano

    def calc_diaria(self):
        return(f'Valor: {self.quant_dia * 30}')
    

    def add_veiculo(self,placa):

        placas = []



        placas.append(placa)




        



