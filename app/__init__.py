from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .database import db
from .models import User, Task

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)

    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)
    return app

from routes import main, auth, tasks