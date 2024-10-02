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

@app.route('/getUsers', methods=['GET'])
def get_users():
    return user_handler.get_users()

@app.route('/getUserById/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return user_handler.get_user_by_id(id)

@app.route('/addFavorite', methods=['POST'])
def add_favorite():
    return user_handler.add_favorite()

@app.route('/deleteFavorite', methods=['DELETE'])
def delete_favorite():
    return user_handler.delete_favorite()


# --------- episodes ---------

@app.route('/createEpisodes', methods=['POST'])
def create_episodes():
    return episode_handler.create_episodes()

@app.route('/getEpisodes', methods=['GET'])
def get_episodes():
    return episode_handler.get_episodes()

@app.route('/getEpisode/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    return episode_handler.get_episode_by_id(id)


# --------- characters ---------

@app.route('/createCharacters', methods=['POST'])
def create_character():
    return character_handler.create_characters()

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

@app.route('/getLocation/<int:id>', methods=['GET'])
def get_location_by_id(id):
    return location_handler.get_location_by_id(id)


if __name__ == '__main__': 
    app.run('localhost', port=3000, debug=True)
