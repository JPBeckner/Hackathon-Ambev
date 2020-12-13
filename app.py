# server
from json import loads  # , dumps

from flask import Flask, request, make_response, jsonify
from flask_mysqldb import MySQL

from db import *
from log import Logger
from models import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = db_name
app.config['MYSQL_PORT'] = port

_db = MySQL(app)

# cliente_dao = ClienteDAO(_db)
# cronograma_dao = CronogramaDAO(_db)
# local_entrega_dao = LocalEntregaDAO(_db)
# pedido_dao = PedidoDAO(_db)
# produto_dao = ProdutoDAO(_db)
# produto_pedido_dao = ProdutoPedidoDAO(_db)
# tipo_transporte_dao = TipoTransporteDAO(_db)
# transporte_dao = TransporteDAO(_db)

log = Logger()

# TODO:
#   links: https://towardsdatascience.com/build-a-web-data-dashboard-in-just-minutes-with-python-d722076aee2b


@app.route("/teste", methods=['GET'])
def teste():
    log.logger.info("[GET] </teste>")
    log.logger.info("Log do método do endpoint de teste.")
    return make_response(jsonify({'teste': 'Sucesso'}), 200)


@app.route("/dados_dashboard", methods=['GET'])
def dados_dashboard():
    try:
        # gráficos:
        # frota
        # subprodutos
        # comparativode lucros
        return
    except Exception as exc:
        log.logger.exception("Erro ao carregar dados do dashboard.", exc_info=exc)
        return make_response(jsonify({"erro": "Houve um problema para carregar os dados."}))


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
