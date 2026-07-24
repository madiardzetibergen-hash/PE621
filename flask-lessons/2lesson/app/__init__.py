from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import products_bp

    app.register_blueprint(
        products_bp,
        url_prefix="/api"
    )
    return app