from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Episode, Character, Location, Favorites
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/createUser', methods=['POST'])
def create_user():
  data = request.json
  user = User()

  user.name = data['name']
  user.last_name = data['last_name']
  user.email = data['email']
  user.password = data['password']

  db.session.add(user)
  db.session.commit()

  return {
    "message": "User created successfully",
  }, 201


@app.route("/getUserById/<int:id>", methods=['GET'])
def get_user_by_id(id):
  user = User.query.filter_by(id=id).first()
  return ({
    "status": "success",
    "data": user.serialize()
  }), 200


@app.route("/getUsers", methods=['GET'])
def get_user():
  users = User.query.all()
  users_serializados = [user.serialize() for user in users]

  return jsonify({
    "status": "success",
    "data": users_serializados
  }), 200

# EPISODE 

@app.route('/createEpisodes', methods=['POST'])
def create_episodes():
  data = request.json

  for new_episode in data["episodes"]:
    episode = Episode()
    episode.name = new_episode['name']
    episode.air_date = new_episode['air_date']
    episode.episode = new_episode['episode']

    db.session.add(episode)

  db.session.commit()

  return {
    "message": "Episode created successfully",
  }, 201

# CHARACTERS 

@app.route('/createCharacter', methods=['POST'])
def create_character():
  data = request.json

  for new_character in data["characters"]:
    character = Character()
    character.name = new_character['name']
    character.status = new_character['status']
    character.gender = new_character['gender']
    character.species = new_character['species']
    character.origin = new_character['origin']
    character.location = new_character['location']
    character.episode = new_character['episode']

    db.session.add(character)

  db.session.commit()

  return {
    "message": "characters created successfully",
  }, 201


# LOCATIONS 

@app.route('/createLocations', methods=['POST'])
def create_locations():
  data = request.json

  for new_location in data["locations"]:
    location = Location()
    location.name = new_location['name']
    location.location_type = new_location['type']
    location.dimension = new_location['dimension']
    location.url = new_location['url']

    db.session.add(location)

  db.session.commit()

  return {
    "message": "Locations created successfully",
  }, 201

if __name__ == '__main__': 
    app.run('localhost', port=3000, debug=True)