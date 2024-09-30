from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db 
from handlers import user_handler, episode_handler, character_handler, location_handler

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# --------- index ---------
@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello World</h1><p>Running in Port:3000</p>'


# ------- users  ---------
@app.route('/createUser', methods=['POST'])
def create_user():
    return user_handler.create_user()

@app.route('/getUserById/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return user_handler.get_user_by_id(id)

@app.route('/getUsers', methods=['GET'])
def get_users():
    return user_handler.get_users()


# --------- episodes ---------
@app.route('/createEpisodes', methods=['POST'])
def create_episodes():
    return episode_handler.create_episodes()


# --------- characters ---------
@app.route('/createCharacter', methods=['POST'])
def create_character():
    return character_handler.create_character()

@app.route('/getCharacters', methods=['GET'])
def get_characters():
    return character_handler.get_characters()

@app.route('/character/<int:id>', methods=['GET'])
def get_character_by_id(id):
    return character_handler.get_character_by_id(id)


# --------- locations ---------
@app.route('/createLocations', methods=['POST'])
def create_locations():
    return location_handler.create_locations()

@app.route('/getLocations', methods=['GET'])
def get_locations():
    return location_handler.get_locations()


if __name__ == '__main__': 
    app.run('localhost', port=3000, debug=True)
