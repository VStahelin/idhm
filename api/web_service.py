from flask import Flask, request, jsonify

from idhm.controllers.apiCidadeController import getUltimoStatusCidade

app = Flask(__name__)


# http://127.0.0.1:5000/cidades/?city=sao pedro de alcantara&uf=uf
@app.route('/cidades/', methods=['GET'])
def home():
    bar = request.args.to_dict()
    print(bar)
    print(bar.__getitem__("city"))
    return bar, 200


@app.route('/cidades/<string:uf>/<string:cidade>', methods=['GET'])
def aa(uf, cidade):
    try:
        json = getUltimoStatusCidade(cidade, uf)
        if len(json) == 0:
            return 'bad request', 400
        return getUltimoStatusCidade(cidade, uf), 200
    except:
        return 'bad request', 400


def up_api():
    app.run(debug=True)


if __name__ == "__main__":
    up_api()
