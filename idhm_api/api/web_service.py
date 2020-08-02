from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

from idhm_api.controllers.apiCidadeController import getUltimoStatusCidade, getGraficoStatusCidade, \
    getStatusGeralEstados, getStatusGeralConfirmadosBrasilGeoChart, getStatusGeralEstadosIndexadoPorNome

app = Flask(__name__, template_folder='../WEB-INF/templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# http://127.0.0.1:5000/cidades/?city=sao pedro de alcantara&uf=uf
@app.route('/cidades/', methods=['GET'])
@cross_origin()
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
@cross_origin()
def aa(uf, cidade):
    try:
        json = {'encode': "utf-8", 'values': getUltimoStatusCidade(cidade, uf)}
        if len(json['values']) == 0:
            return 'bad request', 400
        return json, 200
    except:
        return 'bad request', 400


# http://127.0.0.1:5000/cidades/historico/sc/florianopolis
@app.route('/cidades/historico/<string:uf>/<string:cidade>', methods=['GET'])
@cross_origin()
def historico(uf, cidade):
    try:
        json = {'encode': "utf-8", 'status': getGraficoStatusCidade(cidade, uf)}
        if len(json['status']) == 0:
            return 'bad request', 400
        return json, 200
    except:
        return 'bad request', 400


# http://127.0.0.1:5000/Brasil/QuadroGeral/IndexadoPorEstado
@app.route('/Brasil/QuadroGeral/IndexadoPorEstado', methods=['GET'])
@cross_origin()
def quadroGeral():
    try:
        return getStatusGeralEstadosIndexadoPorNome(), 200
    except:
        return 'bad request', 400


# http://127.0.0.1:5000/Brasil/QuadroGeral/GeoChart/Confirmados
@app.route('/Brasil/QuadroGeral/GeoChart/Confirmados', methods=['GET'])
@cross_origin()
def quadroGeralGeoChartConfirmados():
    try:
        return getStatusGeralConfirmadosBrasilGeoChart(), 200
    except:
        return 'bad request', 400



def up_api():
    app.run(debug=True)


if __name__ == "__main__":
    up_api()
