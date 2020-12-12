# server
from flask import Flask, request, make_response, jsonify
from json import loads, dumps

app = Flask(__name__)


@app.route("/teste", methods=['GET'])
def teste():
    return {'teste': 'teste'}


@app.route("/liberar_pedido", methods=['POST'])
def liberar_pedido():
    try:
        request_body: dict = loads(request.data)
        return make_response(jsonify({'sucess': 'Pedido liberado com sucesso'}), 200)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
