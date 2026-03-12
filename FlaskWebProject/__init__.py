"""
The Flask application package.
"""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix  # <-- Add this

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Fix proxy so url_for(_external=True) generates HTTPS URLs on Azure
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Initialize extensions
Session(app)
db = SQLAlchemy(app)

login = LoginManager()
login.init_app(app)
login.login_view = 'login'

# Logging configuration
if not app.debug:
    file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=5)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] in %(module)s: %(message)s'
    )
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask startup')

# Import views and models
import FlaskWebProject.views
