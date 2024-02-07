from flask import request, jsonify,render_template, redirect, url_for

from app import app
from models import Usuario, Avaliacoes, Usuario_negocio, Promocoes, Atracoes, ItemCardapio, Cardapio, Cinema, Sala, Sessao, Filme, Negocio_alimentacao, Ponto_turistico, Loja


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for the login route
    return render_template('login.html')


@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify([str(usuario) for usuario in Usuario.usuarios])

@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    usuario = Usuario(data['nome'], data['email'], data['dataNascimento'], data['quantidadePontos'])
    return jsonify(str(usuario)), 201

@app.route("/avaliacoes", methods=["GET"])
def get_avaliacoes():
    return jsonify(Avaliacoes.avaliacoes)

@app.route("/negocios", methods=["GET"])
def get_negocios():
    return jsonify([str(negocio) for negocio in Usuario_negocio.negocios])

@app.route("/promocoes", methods=["GET"])
def get_promocoes():
    return jsonify([str(promocao) for promocao in Promocoes.promocoes])

@app.route("/atracoes", methods=["GET"])
def get_atracoes():
    return jsonify([str(atracao) for atracao in Atracoes.atracoes])

@app.route("/cardapio", methods=["GET"])
def get_cardapio():
    return jsonify([str(item.getNome()) + " - R$" + str(item.getPreco()) for item in Cardapio.itens])

@app.route("/salas", methods=["GET"])
def get_salas():
    return jsonify([str(sala) for sala in Sala.salas])

@app.route("/sessoes", methods=["GET"])
def get_sessoes():
    return jsonify([str(sessao) for sessao in Sessao.sessoes])

@app.route("/filmes", methods=["GET"])
def get_filmes():
    return jsonify([str(filme) for filme in Filme.filmes])

@app.route("/negocios_alimentacao", methods=["GET"])
def get_negocios_alimentacao():
    return jsonify([str(negocio) for negocio in Negocio_alimentacao.negocios_alimentacao])

@app.route("/pontos_turisticos", methods=["GET"])
def get_pontos_turisticos():
    return jsonify([str(ponto) for ponto in Ponto_turistico.pontos_turisticos])

@app.route("/lojas", methods=["GET"])
def get_lojas():
    return jsonify([str(loja) for loja in Loja.lojas])

if __name__ == "__main__":
    app.run(debug=True)