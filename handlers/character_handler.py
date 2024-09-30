from flask import request, jsonify
from models import db, Character
import json

def create_characters():
    data = request.json

    for new_character in data["characters"]:
        character = Character()
        character.name = new_character['name']
        character.status = new_character['status']
        character.species = new_character['species']
        character.type = new_character['type']
        character.gender = new_character['gender']
        character.origin = json.dumps(new_character['origin'])
        character.location = json.dumps(new_character['location'])
        character.image = new_character['image']
        character.episodes = json.dumps(new_character['episode'])
        character.url = new_character['url']

        db.session.add(character)

    db.session.commit()

    return {
        "message": "Characters created successfully",
    }, 201

def get_characters():
    characters = Character.query.all()
    serialized_characters = []

    for character in characters:
        serialized_character = character.serialize()
        serialized_character['origin'] = json.loads(serialized_character['origin'])
        serialized_character['location'] = json.loads(serialized_character['location'])
        serialized_character['episodes'] = json.loads(serialized_character['episodes'])
        serialized_characters.append(serialized_character)

    return jsonify({
        "results": serialized_characters
    }), 200

def get_character_by_id(id):
    character = Character.query.filter_by(id=id).first()
    character_serialized = character.serialize()
    character_serialized["origin"] = json.loads(character_serialized["origin"])
    character_serialized["location"] = json.loads(character_serialized["location"])
    character_serialized["episodes"] = json.loads(character_serialized["episodes"])
    return jsonify({
        "results": character_serialized
    }), 200
