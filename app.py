from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Episode, Character, Location, Favorites
from flask_cors import CORS
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# ------------  USER ENDPOINTS ----------------

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

# ------------  EPISODE ENDPOINTS ----------------

@app.route('/createEpisodes', methods=['POST'])
def create_episodes():
    data = request.json

    for new_episode in data["episodes"]:
      episode = Episode()
      episode.name = new_episode['name']
      episode.air_date = new_episode['air_date']
      episode.episode = new_episode['episode']
      episode.url = new_episode['url']

      # Convert to string using json.dumps
      episode.characters = json.dumps(new_episode["characters"])

      db.session.add(episode)

    db.session.commit()

    return {
      "message": "Episode created successfully",
    }, 201

# ---------------- CHARACTERS ENDPOINTS ----------------

@app.route('/createCharacter', methods=['POST'])
def create_character():
    data = request.json

    for new_character in data["characters"]:
        character = Character()
        character.name = new_character['name']
        character.status = new_character['status']
        character.species = new_character['species']
        character.type = new_character['type']
        character.gender = new_character['gender']
        
        # Convert to string using json.dumps
        character.origin = json.dumps(new_character['origin'])  
        character.location = json.dumps(new_character['location'])  
        character.image = new_character['image']
        character.episodes = json.dumps(new_character['episode'])  
        character.url = new_character['url']

        db.session.add(character)

    db.session.commit()

    return {
      "message": "characters created successfully",
    }, 201

@app.route("/getCharacters", methods=['GET'])
def get_characters():
    characters = Character.query.all()
    serialized_characters = []

    for character in characters:
        serialized_character = character.serialize()
        
        # Deserialize fields that are in JSON format
        serialized_character['origin'] = json.loads(serialized_character['origin'])
        serialized_character['location'] = json.loads(serialized_character['location'])
        serialized_character['episodes'] = json.loads(serialized_character['episodes'])
        
        serialized_characters.append(serialized_character)

    return jsonify({
        "status": "success",
        "data": serialized_characters
    }), 200

# CHARACTER BY ID
@app.route("/character/<int:id>", methods=['GET'])
def get_character_by_id(id):
    character = Character.query.filter_by(id=id).first()
    character_serialized = character.serialize()

    # Deserialize fields that are in JSON format
    character_serialized["episodes"] = json.loads(character_serialized["episodes"])
    character_serialized["location"] = json.loads(character_serialized["location"])
    character_serialized["origin"] = json.loads(character_serialized["origin"])
    return ({
      "status": "success",
      "data": character_serialized
    }), 200

# ---------------- LOCATIONS ENDPOINTS ----------------

@app.route('/createLocations', methods=['POST'])
def create_locations():
    data = request.json

    for new_location in data["locations"]:
      location = Location()
      location.name = json.dumps(new_location['name'])
      location.type = json.dumps(new_location['type'])
      location.dimension = json.dumps(new_location['dimension'])
      location.residents = json.dumps(new_location['residents'])
      location.url = json.dumps(new_location['url'])

      db.session.add(location)

    db.session.commit()

    return {
      "message": "Locations created successfully",
    }, 201

@app.route('/getLocations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    serialized_locations = []

    for location in locations:
      serialized_location = location.serialize()
      serialized_location["residents"] = json.loads(serialized_location["residents"])

      serialized_locations.append(serialized_location)

    return jsonify({
        "status": "success",
        "data": serialized_locations
    }), 200

if __name__ == '__main__': 
    app.run('localhost', port=3000, debug=True)