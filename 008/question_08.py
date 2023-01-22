from flask import Flask, jsonify, request
app = Flask(__name__)

contador = 0

@app.route('/contador', methods=['GET'])
def get_contador():
    global contador
    return jsonify(numero=contador), 200

@app.route('/contador', methods=['POST'])
def post_contador():
    dado = request.get_json()
    global contador
    contador = dado["numero"]
    return jsonify(numero=contador), 201

@app.route('/contador/incrementa', methods=['PUT'])
def incrementa_contador():
    global contador
    contador += 1
    return jsonify(numero=contador), 202

@app.route('/contador', methods=['DELETE'])
def zerar_contador():
    global contador
    contador = 0
    return jsonify(numero=contador), 202

if __name__ == '__main__':
    app.run(debug=True)
