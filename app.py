from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})

app.run()