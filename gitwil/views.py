from gitwil import app
from flask import render_template, request, jsonify

@app.route('/')
def homepage():
    user = 'Manin'
    idade = 22
    context = {
        'user': user,
        'idade': idade
    }
    return render_template('index.html', context = context)

@app.route('/graficos')
def pag():
    return "simboraaaa"

respostas = []
@app.route('/resposta', methods=['POST'])
def receber_resposta():
    data = request.get_json()
    resposta = data.get('resposta')
    print("Resposta recebida:", resposta)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip not in respostas:
        respostas.append(ip)
    else:
        return jsonify({"mensagem" :"Resposta não registrada, você já respondeu {}".format(resposta)})
    return jsonify({'mensagem': f'Recebido: {resposta}'})