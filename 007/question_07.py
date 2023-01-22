from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    x = dados["x"]
    y = dados["y"]
    resultado = x + y
    return jsonify(resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
