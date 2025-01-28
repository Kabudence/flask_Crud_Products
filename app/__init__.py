from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Inicializar extensiones
    db.init_app(app)

    # Configurar CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Registrar el Blueprint
    from app.crud_productos import bp as crud_productos_bp
    app.register_blueprint(crud_productos_bp, url_prefix="/api/productos")

    return app
