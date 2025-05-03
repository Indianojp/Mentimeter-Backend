from gitwil import app
from flask import render_template, request, jsonify

@app.route('/')
def homepage():
    return render_template('index.html')

respostas = []
@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()
    resposta = data.get('resposta')
    print("Resposta recebida:", resposta)
    ip = request.remote_addr
    if ip not in respostas:
        respostas.append(ip)
    else:
        return jsonify({"mensagem" :"Resposta não registrada, você já respondeu {}".format(resposta)})
    return jsonify({'mensagem': f'Recebido: {resposta}'})