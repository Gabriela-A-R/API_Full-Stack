from flask import Flask, jsonify, request

usuarios = {
    "user":[{
        'nome': "Ana", 
        'email': "ana@gmail.com", 
        'id_user': 1
    }]
}

def novoID():
    dici_usuarios = usuarios["user"]

    if not dici_usuarios:
        return 1
    
    ultimoID = max(user["id_user"] for user in dici_usuarios)
    return ultimoID + 1
        

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def create_user():
    dados = request.json
    dici_usuarios = usuarios["user"]

    for user in dici_usuarios:
        if user["id_user"] == dados["id_user"]:
            return jsonify({"erro": "ID já existe."}), 400
        
    usuario = {
        "id_user": novoID(),
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios["user"].append(usuario)
    return jsonify(usuario), 201


@app.route('/users', methods=['GET'])
def get_users():
    dados = usuarios["user"]
    return jsonify(dados)


@app.route('/users/<int:id_user>', methods=['GET'])
def getid_users(id_user):
    for user in usuarios["user"]:
        if user["id_user"] == id_user:
            return jsonify(user)
    return jsonify({"erro": "Usuário não encontrado!"}), 404


@app.route('/users/<int:id_user>', methods=['PUT'])
def atualizar_users(id_user):
    dici_usuarios = usuarios["user"]
    
    for user in dici_usuarios:
        if user["id_user"] == id_user:
            dadosUser = request.json
            user["nome"] = dadosUser["nome"]
            user["email"] = dadosUser["email"]
            return jsonify(user)
    
    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.route('/users/<int:id_user>', methods=['DELETE'])
def delete_users(id_user):
    dici_usuarios = usuarios["user"]
    for user in dici_usuarios:
        if user["id_user"] == id_user:
            dici_usuarios.remove(user)
            return jsonify({"mensagem": "Usuário deletado com sucesso!"}), 200
    
    return jsonify({"erro": "Usuário não encontrado."}), 404


if __name__ == '__main__':
    app.run(debug=True)
