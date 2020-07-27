from flask import Flask, request, jsonify

from idhm.controllers.apiCidadeController import getUltimoStatusCidade

app = Flask(__name__)


# http://127.0.0.1:5000/cidades/?city=sao pedro de alcantara&uf=uf
@app.route('/cidades/', methods=['GET'])
def home():
    bar = request.args.to_dict()
    try:
        json = {'encode': "utf-8", 'values': getUltimoStatusCidade(bar.__getitem__("city"), bar.__getitem__("uf"))}
        if len(json['values']) == 0:
            return 'bad request', 400
        return json, 200
    except:
        return 'bad request', 400


# http://127.0.0.1:5000/cidades/sc/florianopolis
@app.route('/cidades/<string:uf>/<string:cidade>', methods=['GET'])
def aa(uf, cidade):
    try:
        json = {'encode': "utf-8", 'values': getUltimoStatusCidade(cidade, uf)}
        if len(json['values']) == 0:
            return 'bad request', 400
        return json, 200
    except:
        return 'bad request', 400


def up_api():
    app.run(debug=True)


if __name__ == "__main__":
    up_api()
