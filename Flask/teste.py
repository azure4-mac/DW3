from flask import Flask
# import requests
# import datetime
# from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/users")
def users():
    return "Seja bem ao sistema de usuários!"

@app.route("/users/<id_user>")
def user_preview(id_user):
    if id_user == '1':
        return "Seja bem vindo! Aluno do 1 ano do IFC"
    elif id_user == '2':
        return "Seja bem vindo! Aluno do 2 ano do IFC"
    elif id_user == '3':
        return "Seja bem vindo! Aluno do 3 ano do IFC"
    else:
        return "Usuário não encontrado!", 404