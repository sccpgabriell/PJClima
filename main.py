from flask import Flask, jsonify, request, make_response
#importa o banco de dados
from by import Clima

app = Flask('clima')

#primeiro metodo - visualizar dados (get)
#app.route é para definir que essa funcao é uma rota para que o flask ente
@app.route('/clima', methods=['GET'])
def get_clima():
    return Clima

#primeiro metodo parte 2 - visualizar dados por id (get / id)
@app.route('/clima/<int:id>', methods=['GET'])
def get_clima_id(id):
    for clima in Clima:
        if clima.get('id') == id:
            return jsonify(clima)


#segundo metodo - criar novos dados (post)
@app.route('/clima', methods=['POST'])
def criar_clima():
    clima = request.json
    Clima.append(clima)
    return make_response(
        jsonify(mensagem='Clima cadastrado com sucesso',
                clima=clima
                )
    )
#terceiro metodo - editar dados (put)
@app.route('/clima/<int:id>', methods=['PUT'])
def editar_clima_id(id):
    clima_alterado= request.get_json()
    for indice, clima in enumerate(Clima):
        if clima.get('id') == id:
            Clima[indice].update(clima_alterado)
            return jsonify(Clima[indice])
        
#quarto metodo - deletar dados (delete)
@app.route('/clima/<int:id>', methods=['DELETE'])
def excluir_clima(id):
    for indice, clima in enumerate(Clima):
        if clima.get('id') == id:
            del Clima[indice]
            return jsonify({"mensagem:": "Clima excluido com sucesso"})

app.run(port=5000, host='localhost')