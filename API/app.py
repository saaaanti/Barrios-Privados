from barrios import Barrios
from flask import Flask, jsonify, request
from flask_cors import CORS

barrios = Barrios("./API/barrioswerb.sqlite3")

barrios.crearTablas()
barrios.insertarMuestras()
barrios.actualizar()


app = Flask(__name__)

CORS(app)


@app.route("/lotes")
def lotes():
    datos = barrios.fetchApi(
        """SELECT l.lote_id, l.lote_manz_id, p.prop_nombre || ' ' || p.prop_apellido, l.lote_m_frente, l.lote_m_prof, l.lote_luz_bool, l.lote_agua_bool, l.lote_asf_bool, l.lote_esq_bool
        FROM Lotes l
        LEFT JOIN  PropLote pl on pl.pl_lote_id = l.lote_id
        LEFT JOIN Propietarios p on p.prop_id = pl.pl_prop_id"""
    )
    print("Aca con lotes")
    return jsonify(datos)


@app.route("/propietarios")
def propietarios():
    datos = barrios.fetchApi(
        """SELECT p.*, (SELECT count(pl.pl_id) from PropLote pl where pl_prop_id = p.prop_id)
        FROM Propietarios p"""
    )

    return jsonify(datos)


@app.route("/consumos")
def consumos():
    datos = barrios.fetchApi("SELECT * FROM Consumos")
    return jsonify(datos)


@app.route("/costos")
def costos():
    datos = barrios.fetchApi("SELECT * FROM Costos")
    return jsonify(datos)


@app.route("/cargar/<tabla>", methods=["POST"])
def form(tabla):
    datos = request.form.to_dict()

    keys = ",".join(datos.keys())
    lista = list(datos.values())

    signos = ""
    for i in range(len(datos.keys()) - 1):
        signos += "?,"
    signos += "?"

    barrios.insertar(f"INSERT INTO {tabla} ({keys}) VALUES ({signos}) ", lista)
    print("Cargamos algo ponele")
    return "ponele que "


app.run(debug=True, use_reloader=False)
