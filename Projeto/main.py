from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/contatos")
def contatos():
    return "Seja bem-vindo ao sistema de contatos!"

@app.route("/empresa")
def empresa():
    return "Seja bem-vindo ao sistema de empresa!"

@app.route("/trabalhe-conosco")
def trabalhe_conosco():
    return "Seja bem-vindo ao sistema de trabalhe conosco!"

if __name__ == "__main__":
    app.run(debug=True)
