"""
The flask application package.
"""
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# Initialize extensions (without app)
db = SQLAlchemy()
login = LoginManager()
sess = Session()

def create_app():
    """Flask application factory."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    login.init_app(app)
    login.login_view = 'login'
    sess.init_app(app)

    # -----------------------
    # Logging Configuration
    # -----------------------
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10*1024*1024, backupCount=5)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask app startup')

    # Import routes/views
    import FlaskWebProject.views
    return app
