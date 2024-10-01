from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app,db)
db.init_app(app)


@app.route('/')

def index():
    return"Welcome to flask"

@app.route('/users/<username>')
def getUsername(username):
    return f"Welcome to flask development {username}"


if __name__ == '__main__':
    app.run(port=5500,debug=True)