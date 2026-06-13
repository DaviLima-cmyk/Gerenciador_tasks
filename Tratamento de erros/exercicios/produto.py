from flask import Flask,jsonify



class Produto:
    def __init__(self,nome,preco,quant):
            self._nome = nome
            self._preco = preco
            self._quant = quant

    @property

    def nome(self):
          return(f"{self._nome}")
    @nome.setter
    def nome(self,entrada):
          
        try:
               if not isinstance(entrada,str) or any(key.digit() for key in entrada):
                    raise ValueError("nao pode ter numero")


        except ValueError as e:
             print(f"Nome invalido,{e}")

        else:
             self._nome = entrada

        finally:
             print("Tentativa de atualizacao de nome encerrada")
    @property

    def preco(self):
         return(f"{self._preco}")
    
    @preco.setter

    def preco(self,valor):
          try:
               if not valor > 0:
                    raise ValueError
               elif not isinstance(valor,(float,int)):
                    raise ValueError
          except ValueError as e:
               print(f"Entrada invalida,{e}")

          else:
               self._preco = valor

          finally:
               print("Tentativa de Atualizacao de valor realizada")

    @property

    def quant(self):
     return(f"{self._quant}")
    
    @quant.setter

    def quant(self,valor):
          try:
              if valor < 0:
                   raise ValueError
          except ValueError as e:
              print(f"Valor informado invalido,{e}")
              
          else:
              self._quant = valor
          finally:
               print("Tentativa de alteracao de valor realizada")
                                      

    def obter_info(self):
         return(f'{self._nome} {self._preco} {self._quant}')
    
    def gerar_json(self):
         return{
         "nome":self._nome,
         "preco":self._preco,
         "quant":self._quant
         }
    

p1 = Produto("Console",40.0,2)
    
app = Flask(__name__)

@app.route('/api/product',methods = ['GET'])
def get_produto():
     return jsonify(p1.gerar_json())

if __name__ == "__main__":
     app.run(debug=True)
         
    

    
         