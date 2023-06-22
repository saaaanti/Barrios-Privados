import sqlite3 as sql


class Barrios:
    def __init__(self):
        self.db = sql.connect("barrios.sqlite3")
        self.cur = self.db.cursor()

    def crearTablas(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Costos (
				seguridad INTEGER,
				kw INTEGER,
				m3_agua INTEGER,
				m3_gas INTEGER,
				total_luz INTEGER,
				mf_agua INTEGER,
				mf_asf INTEGER,
				vehiculos INTEGER,
				m2_valor INTEGER
			)"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Consumos (
				lot INTEGER,
				man INTEGER,
				nombre VARCHAR,
				seguridad FLOAT,
				luz FLOAT,
				agua FLOAT,
				gas FLOAT,
				luz_publica FLOAT,
				f_agua FLOAT, f_asf FLOAT, vehiculo FLOAT, terreno FLOAT
			)"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Propietarios (
				nomape VARCHAR,
				lote INTEGER,
				manzana INTEGER,
				fecha INTEGER,
				sup_cub INTEGER,
				habitantes INTEGER,
				vehiculos INTEGER,
				cons_luz INTEGER,
				cons_agua INTEGER,
				cons_gas INTEGER
			)"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Lotes (
				numero INTEGER,
				manzana INTEGER,
				m_frente INTEGER,
				m_prof INTEGER,
				luz INTEGER,
				agua INTEGER,
				asf INTEGER,
				esq INTEGER,
				lote_id INTEGER
			)"""
        )

    def fetchDatos(self, query: str):
        self.cur.execute(query)
        a = self.cur.fetchall()
        print("Tirando", a)
        return a

    def insertarMuestras(self):
        if self.fetchDatos("SELECT * FROM Costos"):
            self.cur.execute(
                "INSERT INTO Costos VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    30000,
                    60,
                    30,
                    45,
                    80000,
                    40,
                    70,
                    10000,
                    60000,
                ),
            )

        prop_data = [
            ["Perez Luis", 1, 1, 20160922, 600, 2, 1, 0, 2400, 1500],
            ["Perez Luis", 2, 1, 20160922, 830, 0, 0, 1100, 0, 0],
            ["Martinez Marcos", 1, 2, 20181204, 230, 4, 2, 1200, 200, 2300],
            ["Gomez Lucas", 1, 3, 20220431, 0, 0, 0, 0, 1400, 0],
            ["Perez Luis", 2, 2, 20210212, 0, 0, 0, 0, 0, 0],
            ["Perez Luis", 2, 3, 20200512, 700, 5, 3, 0, 4230, 3400],
        ]

        if self.fetchDatos("SELECT * FROM Propietarios") == []:
            self.cur.executemany(
                "INSERT INTO Propietarios VALUES (?,?,?,?,?,?,?,?,?,?)", prop_data
            )

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

    def a(self):
        return "1023124"


b = Barrios()
b.crearTablas()
b.insertarMuestras()
