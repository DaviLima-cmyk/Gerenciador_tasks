#ultilizado para aplicacoes web

#primeiro codigo

# o modulo app.py e semelhante ao main

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods = ['GET','POST']) # tudo que ta aqui vai ser execultado chamado la no server
def Login():
    if request.method == 'POST':
        name = request.form['NomeUser']
        email = request.form['EmailUser']
        senha = request.form['PasswordUser']
        return(f"ola{name},seu email:{email} e  Senha:{senha} fora requisitados via POST")
    return render_template('Cadastro.html')
    
if __name__ == '__main__': # verifica se o script nao esta sendo importado em outro modulo
    app.run(debug = True)