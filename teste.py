from flask import Flask, request, jsonify

app = Flask(__name__)

lista_alunos = [
    {"id": 1, "name": "azure"},
    {"id": 2, "name": "gui"},
    {"id": 3, "name": "js"},
    {"id": 4, "name": "mezzo"},
]

@app.route("/", methods=["GET"])
def listar():
    return jsonify(lista_alunos)

@app.route("/", methods=["POST"])
def adicionar():
    novo_aluno = request.json
    lista_alunos.append(novo_aluno)
    return jsonify(novo_aluno)

@app.route("/", methods=["PUT"])
def atualizar():
    dados = request.json
    for aluno in lista_alunos:
        if aluno["id"] == dados["id"]:
            aluno.update(dados)
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"})

@app.route("/", methods=["DELETE"])
def deletar():
    dados = request.json
    global lista_alunos
    lista_alunos = [a for a in lista_alunos if a["id"] != dados["id"]]
    return jsonify({"mensagem": "Aluno removido"})


if __name__ == "__main__":
    app.run(debug=True)
