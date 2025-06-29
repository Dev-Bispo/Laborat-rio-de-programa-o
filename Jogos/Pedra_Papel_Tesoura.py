import random
from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/game', methods=["POST", "GET"])
def game():
    opcao = {'pedra': 1, 'papel': 2, 'tesoura': 3}
    opcaomaquina = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
    resultado = ""
    escolha_maquina = ""
    

    if request.method == 'POST':
        pessoa = request.form.get('botao')
        maquina = random.randint(1, 3)
        escolha_maquina = opcaomaquina[maquina]

        diferenca = opcao[pessoa] - maquina

        if diferenca == 1 or diferenca == -2:
            resultado = "Você ganhou!"
        elif diferenca == -1 or diferenca == 2:
            resultado = "Você perdeu!"
           
            
        else:
            resultado = "Empate!"

    return render_template('PPT.html', resultado=resultado, escolha_maquina=escolha_maquina)
