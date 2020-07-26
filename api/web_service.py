from flask import Flask

app = Flask(__name__)


@app.route('/cidades/<string:nome>', methods=['GET'])
def home(nome):
    return "Hello {}".format(nome), 200


def up_api():
    app.run(debug=True)


if __name__ == "__main__":
    up_api()
