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

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable server-side sessions
Session(app)

# Initialize database
db = SQLAlchemy(app)

# Initialize Flask-Login
login = LoginManager(app)
login.login_view = 'login'

# -----------------------
# Logging Configuration
# -----------------------
if not os.path.exists('logs'):
    os.mkdir('logs')

# Rotating file handler: max 10 MB per file, keep 5 backups
file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10*1024*1024, backupCount=5)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
))
file_handler.setLevel(logging.INFO)

# Add handler to app logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Flask app startup')

# -----------------------
# Import views last
# -----------------------
import FlaskWebProject.views
