from app import app
from routes import auth, main, tasks

if __name__ == '__main__':
    app.run(debug=True)