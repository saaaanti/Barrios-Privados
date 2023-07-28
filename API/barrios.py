import sqlite3 as sql
import os


class Barrios:
    def __init__(self, path: str, eliminar=False):
        if eliminar:
            try:
                os.remove(path)
                print("Eliminando la base de datos en", path)
            except:
                print("No se eliminó la base de datos en", path)

        self.conn = sql.connect(path, check_same_thread=False)
        self.conn.row_factory = sql.Row
        self.cur = self.conn.cursor()

    def crearTablas(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Costos (
                cos_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cos_seguridad FLOAT NOT NULL,
                cos_kw FLOAT NOT NULL,
                cos_m3_agua FLOAT NOT NULL,
                cos_m3_gas FLOAT NOT NULL,
                cos_total_luz FLOAT NOT NULL,
                cos_mf_agua FLOAT NOT NULL,
                cos_mf_asf FLOAT NOT NULL,
                cos_vehiculos FLOAT NOT NULL,
                cos_m2_valor FLOAT NOT NULL,
                cos_mes VARCHAR(6) NOT NULL UNIQUE CHECK(cos_mes like '____-__')
            )"""
        )

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Propietarios (
                prop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                prop_nombre VARCHAR NOT NULL,
                prop_apellido VARCHAR NOT NULL
                
            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Manzanas (
                manz_id INTEGER PRIMARY KEY AUTOINCREMENT
            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Lotes (
                lote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lote_manz_id INTEGER NOT NULL,
                lote_m_frente FLOAT NOT NULL,
                lote_m_prof FLOAT NOT NULL,
                lote_luz_bool BOOLEAN NOT NULL DEFAULT FALSE,
                lote_agua_bool BOOLEAN NOT NULL DEFAULT FALSE,
                lote_asf_bool BOOLEAN NOT NULL DEFAULT FALSE,
                lote_esq_bool BOOLEAN NOT NULL DEFAULT FALSE,
                FOREIGN KEY (lote_manz_id) REFERENCES Manzanas (manz_id)
            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS PropLote (
                pl_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pl_lote_id INTEGER NOT NULL,
                pl_prop_id INTEGER NOT NULL,
                pl_fecha_compra DATE NOT NULL,
                pl_fecha_venta DATE,
                pl_superficie_cub FLOAT NOT NULL,
                pl_habitantes INTEGER NOT NULL,
                pl_vehiculos INTEGER NOT NULL,
                pl_cons_luz FLOAT NOT NULL,
                pl_cons_agua FLOAT NOT NULL,
                pl_cons_gas FLOAT NOT NULL,
                FOREIGN KEY (pl_lote_id) REFERENCES Lotes (lote_id),
                FOREIGN KEY (pl_prop_id) REFERENCES Propietarios (prop_id)


        )"""
        )

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Consumos (
                cons_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cons_lot_id INTEGER NOT NULL,
                cons_prop_id INTEGER NOT NULL,
                cons_cost_id INTEGER NOT NULL ,
                cons_seguridad FLOAT NOT NULL,
                cons_luz FLOAT NOT NULL,
                cons_agua FLOAT NOT NULL,
                cons_gas FLOAT NOT NULL,
                cons_luz_publica FLOAT NOT NULL,
                cons_f_agua FLOAT NOT NULL,
                cons_f_asf FLOAT NOT NULL,
                cons_vehiculo FLOAT NOT NULL,
                FOREIGN KEY (cons_lot_id) REFERENCES Lotes (lote_id),
                FOREIGN KEY (cons_prop_id) REFERENCES Propietarios (prop_id),
                FOREIGN KEY (cons_cost_id) REFERENCES Costos (cos_id),
                CONSTRAINT combinacion UNIQUE (cons_prop_id, cons_lot_id, cons_cost_id)
            )"""
        )
        print("Terminamos de crear las tablas")

    def fetchDatos(self, query: str):
        cur = self.conn.cursor()

        cur.execute(query)
        a = cur.fetchall()
        cur.close()
        return a

    def insertarMuestras(self):
        if self.fetchDatos("SELECT * FROM Costos") == []:
            print("??")
            self.cur.execute(
                "INSERT INTO Costos VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",
                (
                    30000.00,
                    60.00,
                    30.00,
                    45.00,
                    80000.00,
                    40.00,
                    70.00,
                    10000.00,
                    60000.00,
                    "2023-08",
                ),
            )

        prop_data = [
            ["Perez", "Luis"],
            ["Martinez", "Marcos"],
            ["Gomez", "Lucas"],
            ["Perez", "Luis"],
        ]
        if self.fetchDatos("SELECT * FROM Propietarios") == []:
            self.cur.executemany(
                "INSERT INTO Propietarios VALUES (NULL,?,?)", prop_data
            )

        # manz_data = [
        #     [1, "asd"],
        #     [2, "asd"],
        #     [3, "asd"],
        #     [4, "asd"],
        # ]

        if self.fetchDatos("SELECT * FROM Manzanas") == []:
            self.cur.executemany("INSERT INTO Manzanas VALUES (NULL)", [])  # manz_data

        lote_data = [
            [1, 100, 120, 0, 1, 1, 1],
            [1, 110, 90, 1, 0, 1, 0],
            [2, 90, 110, 1, 1, 0, 1],
            [2, 110, 100, 0, 1, 0, 0],
            [3, 85, 100, 0, 0, 1, 1],
            [3, 100, 85, 0, 1, 1, 0],
            [4, 100, 120, 1, 1, 1, 1],
        ]

        if self.fetchDatos("SELECT * FROM Lotes") == []:
            self.cur.executemany(
                "INSERT INTO Lotes VALUES (NULL,?,?,?,?,?,?,?)", lote_data
            )

        prop_lote_data = [
            [1, 1, "2016-09-22", None, 600, 2, 1, 0, 2400, 1500],
            [2, 2, "2016-09-22", None, 830, 0, 0, 1100, 0, 0],
            [3, 2, "2018-12-04", None, 230, 4, 2, 1200, 200, 2300],
            [4, 3, "2022-04-31", None, 0, 0, 0, 0, 1400, 0],
            [5, 4, "2021-02-12", None, 0, 0, 0, 0, 0, 0],
            [6, 3, "2020-05-12", None, 700, 5, 3, 0, 4230, 3400],
        ]

        if self.fetchDatos("SELECT * FROM PropLote") == []:
            self.cur.executemany(
                "INSERT INTO PropLote VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", prop_lote_data
            )

        self.conn.commit()
        print("Insertamos los datos de muestra")

    def actualizar(self, mes):
        # TODO: que pase el mes para cargar o algo
        datos = self.fetchDatos(
            """SELECT l.*, p.*, pl.*
            FROM PropLote pl
            JOIN Propietarios p on pl.pl_prop_id = p.prop_id
            JOIN Lotes l on pl.pl_lote_id = l.lote_id
            """
        )

        mesId = self.fetchDatos(f"SELECT cos_id FROM Costos where cos_mes = '{mes}'")[
            0
        ]["cos_id"]

        costos = self.fetchDatos(f"SELECT * FROM Costos where cos_mes = '{mes}'")
        consumos = self.fetchDatos(f"SELECT * FROM Consumos")

        # ESTA ES UNA SOLUCIÓN MEDIO BRUSCA PERO YA FUE QUEDAAa
        for rowC in consumos:
            for rowP in datos:
                if (
                    str(rowC["cons_cost_id"]) == str(mesId)
                    and str(rowC["cons_prop_id"]) == str(rowP["prop_id"])
                    and str(rowC["cons_lot_id"]) == str(rowP["lote_id"])
                ):
                    print("xd")
                    self.cur.execute(
                        f"DELETE FROM Consumos WHERE cons_cost_id = {mesId} AND cons_prop_id = {rowP['prop_id']} AND cons_lot_id = {rowP['lote_id']}"
                    )

        pago_lot = []
        pago_prop = []
        pago_seguridad = []
        pago_luz = []
        pago_agua = []
        pago_gas = []
        pago_luz_publica = []
        pago_f_agua = []
        pago_f_asf = []
        pago_vehiculo = []
        pago_costos = []

        lotes_construidos = 0
        lotes_luz = 0

        for i in datos:
            # TODO: Optimizar
            if i["pl_superficie_cub"] > 0:
                lotes_construidos += 1

            if i["lote_luz_bool"]:
                lotes_luz += 1

        # TODO: MES

        pago_lote_const = costos[0]["cos_seguridad"] / (len(datos) + lotes_construidos)
        pago_lote_no_const = pago_lote_const * 2

        for i in datos:
            pago_lot.append(i["lote_id"])
            pago_prop.append(i["prop_id"])

            if i["pl_superficie_cub"] > 0:
                pago_seguridad.append(pago_lote_const)
            else:
                pago_seguridad.append(pago_lote_no_const)

            # TODO: MES
            pago_luz.append(costos[0]["cos_kw"] * i["pl_cons_luz"])
            pago_agua.append(costos[0]["cos_m3_agua"] * i["pl_cons_agua"])
            pago_gas.append(costos[0]["cos_m3_gas"] * i["pl_cons_gas"])

            if i["lote_luz_bool"]:
                # TODO: MES
                pago_luz_publica.append(costos[0]["cos_total_luz"] / lotes_luz)
            else:
                pago_luz_publica.append(0)

            if i["lote_esq_bool"]:
                # TODO: MES
                pago_f_agua.append(
                    costos[0]["cos_mf_agua"] * (i["lote_m_frente"] + i["lote_m_prof"])
                )
                pago_f_asf.append(
                    costos[0]["cos_mf_asf"] * (i["lote_m_frente"] + i["lote_m_prof"])
                )
            else:
                pago_f_agua.append(costos[0]["cos_mf_agua"] * (i["lote_m_prof"]))
                pago_f_asf.append(costos[0]["cos_mf_asf"] * (i["lote_m_prof"]))

            pago_vehiculo.append(costos[0]["cos_vehiculos"] * i["pl_vehiculos"])

            pago_costos.append(mesId)

        lista = [
            pago_lot,
            pago_prop,
            pago_costos,
            pago_seguridad,
            pago_luz,
            pago_agua,
            pago_gas,
            pago_luz_publica,
            pago_f_agua,
            pago_f_asf,
            pago_vehiculo,
        ]
        transpuesta = []

        for i in range(len(lista[0])):
            f = []
            for j in range(len(lista)):
                f.append(lista[j][i])
            transpuesta.append(f)

        self.cur.executemany(
            "INSERT INTO Consumos Values (NULL,?,?,?,?,?,?,?,?,?,?,?)", transpuesta
        )

        self.conn.commit()

        print("Actualizamos los datos")

    def fetchApi(self, query):
        datos = self.fetchDatos(query)

        dicc = []
        for i, row in enumerate(datos):
            dicc.append([])
            for key in row.keys():
                # Transformamos 0 y 1 a bool cuando necesitamos
                if key[-4:] == "bool":
                    dicc[i].append({key: bool(row[key])})
                else:
                    dicc[i].append({key: row[key]})
        return dicc

    def insertar(self, query: str, otros: list):
        cur = self.conn.cursor()

        print("Vamos a llamar", query)
        print("con", otros)

        cur.execute(query, otros)
        cur.close()
        self.conn.commit()

    def ejecutar(self, query: str):
        print("El query es ")
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        cur.close()
        self.conn.commit()


if __name__ == "__main__":
    print("Ejecutando de main")
    path = "./barriosTestMain.sqlite3"
    try:
        os.remove(path)
    except:
        print("Jjas")

    b = Barrios(path)
    b.crearTablas()
    b.insertarMuestras()
    b.actualizar("2023-08")
