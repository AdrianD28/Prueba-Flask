from flask import Flask
from db.db import db
from routes.routes import contact
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
app.register_blueprint(contact)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)

