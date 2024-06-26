from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Saludo(db.Model):
    __tablename__ = 'saludo'
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, mensaje):
        self.mensaje = mensaje
