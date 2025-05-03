from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()
    resposta = data.get('resposta')
    print("Resposta recebida:", resposta)
    return jsonify({'mensagem': f'Recebido: {resposta}'})

if __name__ == '__main__':
    app.run(debug=True)
