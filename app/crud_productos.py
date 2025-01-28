from flask import Blueprint, request, jsonify
from app import db
from app.productos import Producto

bp = Blueprint('productos', __name__)  # Elimina url_prefix aquí, ya se gestiona en app.register_blueprint

@bp.route('/', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([producto.to_json() for producto in productos])

@bp.route('/', methods=['POST'])
def agregar_producto():
    datos = request.json
    nuevo_producto = Producto(
        nombre=datos['nombre'],
        precio=datos['precio'],
        stock=datos['stock']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify(nuevo_producto.to_json()), 201

@bp.route('/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Producto.query.get_or_404(id)
    datos = request.json
    producto.nombre = datos['nombre']
    producto.precio = datos['precio']
    producto.stock = datos['stock']
    db.session.commit()
    return jsonify(producto.to_json())

@bp.route('/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado exitosamente'}), 200
