from barrios import Barrios
from flask import Flask, jsonify, request
from flask_cors import CORS

barrios = Barrios("./API/barrioswerb.db")

barrios.crearTablas()
barrios.insertarMuestras()
barrios.actualizar()


app = Flask(__name__)

CORS(app)


@app.route("/lotes")
def lotes():
    datos = barrios.fetchApi("SELECT * FROM Lotes")
    return jsonify(datos)


@app.route("/propietarios")
def propietarios():
    datos = barrios.fetchApi("SELECT * FROM Propietarios")
    return jsonify(datos)


@app.route("/consumos")
def consumos():
    datos = barrios.fetchApi("SELECT * FROM Consumos")
    return jsonify(datos)


@app.route("/costos")
def costos():
    datos = barrios.fetchApi("SELECT * FROM Costos")
    return jsonify(datos)


@app.route("/form", methods=["POST"])
def form():
    print("\n" * 3)
    print(request.form.to_dict())

    # Step 4: Retrieve form data
    #  name = request.form.get("name")
    #  email = request.form.get("email")

    # print(f"Name: {name}")
    # print(f"Email: {email}")

    return "recibimos los datos creo xd"


app.run(debug=True, use_reloader=False)
