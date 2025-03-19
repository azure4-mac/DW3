from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/soma", methods=["POST"])
def somar():
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos["Numero 1:"]
    numero2 = dados_recebidos["Numero 2:"]
    resultado = numero1 + numero2
    return {'resultado': resultado}



if __name__ == "__main__":
    app.run(debug=True)
