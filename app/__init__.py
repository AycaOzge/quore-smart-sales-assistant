from flask import Flask
from flask_cors import CORS

from app.routes import main_bp, api_bp
from app.database import init_db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    init_db(app)

    return app