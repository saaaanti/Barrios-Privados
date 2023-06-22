from barrios import Barrios
from flask import Flask, jsonify
from flask_cors import CORS

barrios = Barrios()

app = Flask(__name__)


CORS(app)


@app.route('/person/')
def hello():

    d = {'name':'Jimit',
                    'address': "hola",
            }
    return jsonify(d)

app.run(debug = True, use_reloader=False)