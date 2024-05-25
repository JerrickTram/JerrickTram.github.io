from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    with app.app_context():a
        from .routes import bp as main_bp
        app.register_blueprint(main_bp)
        db.create_all()

    return app
