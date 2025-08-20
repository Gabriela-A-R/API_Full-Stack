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
    usuario = {
        "nome": dados["nome"],
        "email": dados["email"],
        "id_user": novoID()
    }
    usuarios['user'].append(usuario)
    return jsonify(usuario), 200


@app.route('/users', methods=['GET'])
def get_users():
    dados = usuarios["user"]
    return jsonify(dados)


@app.route('/users/<int:id_user>', methods=['GET'])
def getid_users(id_user):
    for user in usuarios["user"]:
        if user["id_user"] == id_user:
            return jsonify(user)

@app.route('/users/<int:id_user>', methods=['PUT'])
def atualizar_users(id_user):
    dados = request.json
    for user in usuarios["user"]:
        if user["id_user"] == id_user:
            user['nome'] = dados.get('nome', user['nome'])
            user['email'] = dados.get('email', user['email'])
            return jsonify(user), 200


@app.route('/users/<int:id_user>', methods=['DELETE'])
def delete_users(id_user):
    users = usuarios['user']
    for user in users:
        if user['id_user'] == id_user:
            users.remove(user)
            return jsonify({"mensagem": "Deletado"}), 200

if __name__ == '__main__':
    app.run(debug=True)

    