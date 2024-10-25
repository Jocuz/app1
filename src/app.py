import web
import db

urls = (
    '/personas', 'Personas',
)
app = web.application(urls, globals())

class Personas:
    def GET(self):
        db.cursor.execute("SELECT * FROM personas")
        personas = db.cursor.fetchall()
        return web.json(personas)

    def POST(self):
        data = web.input(nombre="", telefono="")
        db.cursor.execute("INSERT INTO personas (nombre, telefono) VALUES (%s, %s) RETURNING id",
                          (data.nombre, data.telefono))
        db.conn.commit()
        return web.json({"id": db.cursor.fetchone()[0], "nombre": data.nombre, "telefono": data.telefono})

if __name__ == "__main__":
    app.run()
