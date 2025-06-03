from flask import Flask
import requests
import datetime
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    # mensagem = request.args.get('mensagem')
    #     printo(mensagem)  

    user = [
        {'id': 1, 'name': 'Alice',
        'email': 'alice@ifc.edu.br',
        'age': 30}]