# server
from flask import Flask, request, make_response, jsonify
from json import loads  # , dumps
from flask_mysqldb import MySQL
from db import *
from log import Logger

app = Flask(__name__)

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = db_name
app.config['MYSQL_PORT'] = port

_db = MySQL(app)

cliente_dao = ClienteDAO(_db)
cronograma_dao = CronogramaDAO(_db)
local_entrega_dao = LocalEntregaDAO(_db)
pedidoa_dao = PedidoDAO(_db)
produto_dao = ProdutoDAO(_db)
produto_pedido_dao = ProdutoPedidoDAO(_db)
tipo_transporte_dao = TipoTransporteDAO(_db)
transporte_dao = TransporteDAO(_db)

log = Logger()


@app.route("/teste", methods=['GET'])
def teste():
    log.logger.info("[GET] </teste>")
    log.logger.info("Log do método do endpoint de teste.")
    return make_response(jsonify({'teste': 'Sucesso'}), 200)


@app.route("/liberar_pedido", methods=['POST'])
def liberar_pedido():
    try:
        request_body: dict = loads(request.data)

        return make_response(jsonify(request_body), 200)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    app.run(host="192.168.0.20", port=8080, debug=True, threaded=True)

