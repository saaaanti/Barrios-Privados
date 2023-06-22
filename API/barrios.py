import sqlite3 as sql
import os


class Barrios:
    def __init__(self, path: str):
        self.conn = sql.connect(path)
        self.cur = self.conn.cursor()

    def crearTablas(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Costos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
				seguridad FLOAT NOT NULL,
				kw FLOAT NOT NULL,
				m3_agua FLOAT NOT NULL,
				m3_gas FLOAT NOT NULL,
				total_luz FLOAT NOT NULL,
				mf_agua FLOAT NOT NULL,
				mf_asf FLOAT NOT NULL,
				vehiculos FLOAT NOT NULL,
				m2_valor FLOAT NOT NULL,
                mes VARCHAR(6) NOT NULL UNIQUE CHECK(mes like '____-__')
			)"""
        )

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Propietarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR NOT NULL,
                apellido VARCHAR NOT NULL,
				lot_id INTEGER,
				fecha_compra DATE,
				superficie_cub FLOAT,
				habitantes INTEGER,
				vehiculos INTEGER,
				cons_luz FLOAT,
				cons_agua FLOAT,
				cons_gas FLOAT,
                FOREIGN KEY (lot_id) REFERENCES Lotes (id)
			)"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Manzanas (
				id INTEGER PRIMARY KEY AUTOINCREMENT
			)"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Lotes (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				manz_id INTEGER NOT NULL,
				m_frente FLOAT NOT NULL,
				m_prof FLOAT NOT NULL,
				usa_luz BOOLEAN NOT NULL,
				usa_agua BOOLEAN NOT NULL,
				usa_asf BOOLEAN NOT NULL,
				usa_esq BOOLEAN NOT NULL,
                FOREIGN KEY (manz_id) REFERENCES Manzanas (id)
			)"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Consumos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lot_id INTEGER NOT NULL,
				prop_id INTEGER NOT NULL,
                cost_id INTEGER NOT NULL,
				seguridad FLOAT NOT NULL,
				luz FLOAT NOT NULL,
				agua FLOAT NOT NULL,
				gas FLOAT NOT NULL,
				luz_publica FLOAT NOT NULL,
				f_agua FLOAT NOT NULL,
                f_asf FLOAT NOT NULL,
                vehiculo FLOAT NOT NULL,
                FOREIGN KEY (lot_id) REFERENCES Lotes (id),
                FOREIGN KEY (prop_id) REFERENCES Propietarios (id),
                FOREIGN KEY (cost_id) REFERENCES Costos (id)
			)"""
        )

    def fetchDatos(self, query: str):
        self.cur.execute(query)
        a = self.cur.fetchall()
        print("Tirando", a)
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
                    "2023-06",
                ),
            )

        prop_data = [
            ["Perez", "Luis", 1, "2016-09-22", 600, 2, 1, 0, 2400, 1500],
            ["Perez", "Luis", 2, "2016-09-22", 830, 0, 0, 1100, 0, 0],
            ["Martinez", "Marcos", 1, "2018-12-04", 230, 4, 2, 1200, 200, 2300],
            ["Gomez", "Lucas", 1, "2022-04-31", 0, 0, 0, 0, 1400, 0],
            ["Perez", "Luis", 2, "2021-02-12", 0, 0, 0, 0, 0, 0],
            ["Perez", "Luis", 2, "2020-05-12", 700, 5, 3, 0, 4230, 3400],
        ]

        if self.fetchDatos("SELECT * FROM Propietarios") == []:
            self.cur.executemany(
                "INSERT INTO Propietarios VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", prop_data
            )
        self.conn.commit()
        return
        lote_data = [
            [1, 1, 100, 120, 0, 1, 1, 1, 1],
            [2, 1, 110, 90, 1, 0, 1, 0, 2],
            [1, 2, 90, 110, 1, 1, 0, 1, 3],
            [2, 2, 110, 100, 0, 1, 0, 0, 4],
            [1, 3, 85, 100, 0, 0, 1, 1, 5],
            [2, 3, 100, 85, 0, 1, 1, 0, 6],
            [1, 4, 100, 120, 1, 1, 2, 2, 7],
        ]

        if self.fetchDatos("SELECT * FROM Lotes") == []:
            self.cur.executemany(
                "INSERT INTO Lotes VALUES (?,?,?,?,?,?,?,?,?)", lote_data
            )

        self.conn.commit()

    def a(self):
        return "1023124"


path = "./barrios1.sqlite3"
try:
    os.remove(path)
except:
    print("Jjas")

b = Barrios(path)
b.crearTablas()
b.insertarMuestras()
