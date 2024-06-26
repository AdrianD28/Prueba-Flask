from flask import blueprints, request, jsonify
from db.db import db
from db.db import Saludo
contact = blueprints.Blueprint('contact', __name__, url_prefix='/api/v1')

@contact.route('/saludos', methods=['POST'])
def agregar_saludo():
    try:
        
        if not request.json or 'mensaje' not in request.json:
            return jsonify({'error': 'El campo mensaje es requerido'}), 400

        mensaje = request.json['mensaje']
        nuevo_saludo = Saludo(mensaje=mensaje)

        db.session.add(nuevo_saludo)
        db.session.commit()

        return jsonify({'mensaje': 'Saludo agregado correctamente.'}), 200
    except Exception as e:
        
        return jsonify({'error': str(e)}), 500
    
@contact.route('/saludos', methods=['GET'])
def obtener_saludos():
    try:

        saludos = Saludo.query.all()
        saludos = list(map(lambda saludo: {'id': saludo.id, 'mensaje': saludo.mensaje}, saludos))
        return jsonify(saludos), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@contact.route('/saludos/<int:id>', methods=['GET'])
def obtener_saludo(id):
    try:
        saludo = Saludo.query.get(id)
        if saludo is None:

            return jsonify({'error': 'Saludo no encontrado'}), 404
        
        return jsonify({'id': saludo.id, 'mensaje': saludo.mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
