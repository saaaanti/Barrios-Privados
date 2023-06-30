from barrios import Barrios
from flask import Flask, jsonify
from flask_cors import CORS

barrios = Barrios("./API/barrioswerb.db")

barrios.crearTablas()
barrios.insertarMuestras()
barrios.actualizar()


app = Flask(__name__)

CORS(app)


@app.route("/")
def hello():
    datos = barrios.fetchApi("SELECT * FROM Propietarios")

    return jsonify(datos)


app.run(debug=True, use_reloader=False)
