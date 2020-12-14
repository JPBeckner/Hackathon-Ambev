# server
from json import loads  # , dumps
from datetime import date

from flask import (
    Flask, request, make_response, jsonify, render_template,
    redirect, flash, session, url_for, Markup
)

from db import *
from log import Logger
from models import *

app = Flask(__name__)

DaoConnectionFactory(app)
_db = DaoConnectionFactory.get_connection()

log = Logger()

# @app.route("/teste", methods=['GET'])
# def teste():
#     log.logger.info("[GET] </teste>")
#     log.logger.info("Log do método do endpoint de teste.")
#     return make_response(jsonify({'teste': 'Sucesso'}), 200)
#
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
#
# @app.route("/login", methods=['GET'])
# def login():
#     proxima = request.json.get('proxima')
#     return render_template('login.html', proxima=proxima)


@app.route("/auth", methods=['POST'])
def auth():
    usuario_dao = UsuarioDAO(_db)
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if not usuario:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))

    if usuario.senha == request.form['senha']:
        session['usuario_logado'] = usuario.id
        flash(f"{usuario.nome} logado com sucesso.")
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)


@app.route("/dados_dashboard", methods=['GET'])
def dados_dashboard():
    try:
        frota = {}
        subprodutos = {}
        comparativo_lucro = {}
        graph_data_dashboard = {
            'frota': frota,
            'sub_protudos': subprodutos,
            'comparativo_lucro': comparativo_lucro
        }

        # frota
        transporte = Transporte()
        transporte_dao = TransporteDAO(_db)
        
        fortas_do_dia = transporte_dao.get

        return
    except Exception as exc:
        log.logger.exception("Erro ao carregar dados do dashboard.", exc_info=exc)
        return make_response(jsonify({"erro": "Houve um problema para carregar os dados."}))


@app.route("/pedidos-dia", methods=['POST'])
def get_pedidos_do_dia():
    try:
        data = request.json
        if not data:
            data = str(date.today())
        pedido = PedidoDAO(_db)
        cronograma = CronogramaDAO(_db)
        pedidos: list = []
        cronogramas_por_data: list = cronograma.get_cronogramas_por_data(data)
        _cronograma: Cronograma
        for _cronograma in cronogramas_por_data:
            id_pedido: str = _cronograma.getIdPedido()
            pedidos.append(pedido.busca_por_id(id_pedido))

        resposta_pedidos = {}
        _pedido: Pedido
        for _pedido in pedidos:
            dados_pedido = {
                _pedido
            }
        return make_response(jsonify(pedidos))
    except Exception as exc:
        log.logger.exception("Erro ao carregar pedidos.", exc_info=exc)
        return make_response(jsonify({"erro": "Houve um problema para carregar os pedidos do dia."}))


@app.route("/historico-pedidos", methods=['POST'])
def get_historico_pedido():
    dados_: dict = {}
    return make_response(jsonify(dados_))


@app.route("/", methods=[''])
def _():
    dados_: dict = {}
    return make_response(jsonify(dados_))


@app.route("/", methods=[''])
def _():
    dados_: dict = {}
    return make_response(jsonify(dados_))


@app.route("/liberar_pedido", methods=['POST'])
def liberar_pedido():
    try:
        # request_body: dict = loads(request.data)
        # jogo_id = request_body.get('request_id')
        pedido_id = request.form.get('pedido_id')
        if not pedido_id:
            return make_response(jsonify({'erro': 'Códigodo pedido não informado.'}), 406)

        pedido = Pedido(pedido_id)
        produto_pedido = ProdutoPedidoDAO(_db)
        liberado = ProdutoPedido.liberar_pedido(pedido)
        if not liberado:
            return make_response(jsonify({'erro': 'Erro ao liberar o pedido.'}), 500)

        return make_response(jsonify({"mensagem": "Pedido liberado com sucesso."}), 200)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    app.run(host="192.168.0.20", port=8080, debug=True, threaded=True)
