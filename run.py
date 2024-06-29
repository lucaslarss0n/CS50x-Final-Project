from app import create_app, db
from app.routes import auth, main, tasks

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
