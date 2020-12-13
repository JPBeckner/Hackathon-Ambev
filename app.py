# server
from json import loads  # , dumps
from datetime import date

from flask import (
    Flask, request, make_response, jsonify, render_template,
    redirect, flash, session, url_for, Markup
)
from flask_mysqldb import MySQL
from plotly.offline import plot
from plotly.graph_objs import Scatter

from db import *
from log import Logger
from models import *

app = Flask(__name__)

DaoConnectionFactory(app)
_db = DaoConnectionFactory.get_connection()

log = Logger()

# TODO:
#   links: https://towardsdatascience.com/build-a-web-data-dashboard-in-just-minutes-with-python-d722076aee2b


@app.route("/teste", methods=['GET'])
def teste():
    log.logger.info("[GET] </teste>")
    log.logger.info("Log do método do endpoint de teste.")
    return make_response(jsonify({'teste': 'Sucesso'}), 200)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET'])
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route("/auth", methods=['POST'])
def auth():
    cliente_dao = ClienteDAO(_db)
    cliente = cliente_dao.buscar_por_id(request.form['usuario'])
    if not cliente:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))
    # if usuario:
    if cliente.senha == request.form['senha']:
        session['usuario_logado'] = cliente.id
        flash(f"{cliente.nome} logado com sucesso.")
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    # else:


@app.route("/dados_dashboard", methods=['GET'])
def dados_dashboard():
    try:
        # gráficos:
        # frota
        # subprodutos
        # comparativode lucros
        my_plot_div = plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], output_type='div')
        return render_template('teste.html', div_placeholder=Markup(my_plot_div))
    except Exception as exc:
        log.logger.exception("Erro ao carregar dados do dashboard.", exc_info=exc)
        return make_response(jsonify({"erro": "Houve um problema para carregar os dados."}))


@app.route("/pedidos-dia", methods=['POST'])
def get_pedidos_do_dia():
    try:
        # cronogramas_hoje = Cronograma()
        hoje = str(date.today())
        pedido = PedidoDAO()
        cronograma = CronogramaDAO()
        pedidos: list = []
        cronogramas_por_data: list = cronograma.get_cronogramas_por_data(hoje)
        _cronograma: dict
        for _cronograma in cronogramas_por_data:
            id_pedido: str = _cronograma.get('id')
            pedidos.append(pedido.busca_por_id(id_pedido))
        # dados_pedidos = Pedido()
        return make_response(jsonify(pedido))
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
        jogo_id = request.form.get('pedido_id')
        if not jogo_id:
            return make_response(jsonify({'erro': 'Códigodo pedido não informado.'}), 406)

        pedido = Pedido(jogo_id)
        liberado = ProdutoPedido.liberar_pedido(pedido)
        if not liberado:
            return make_response(jsonify({'erro': 'Erro ao liberar o pedido.'}), 500)

        return make_response(jsonify({"mensagem": "Pedido liberado com sucesso."}), 200)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    app.run(host="192.168.0.20", port=8080, debug=True, threaded=True)
