from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir acesso do frontend

@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()
    resposta = data.get('resposta')
    print("Resposta recebida:", resposta)
    return jsonify({'mensagem': f'Recebido: {resposta}'})

if __name__ == '__main__':
    app.run(debug=True)
