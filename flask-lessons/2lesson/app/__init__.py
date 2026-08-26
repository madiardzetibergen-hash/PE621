from flask import Flask
from flask_cors import CORS  # <--- Импортируем CORS


def create_app():
    app = Flask(__name__)
    CORS(app)  # <--- Разрешаем кросс-доменные запросы

    from app.routes import products_bp

    app.register_blueprint(products_bp, url_prefix="/api")
    return app