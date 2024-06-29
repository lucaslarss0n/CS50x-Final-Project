from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from .database import db
from .models import User

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = 'auth_bp.login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    return app
