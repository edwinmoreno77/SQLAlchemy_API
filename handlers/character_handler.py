from flask import request, jsonify
from models import db, Character

def create_characters():
    data = request.json

    for new_character in data["characters"]:
        character = Character()
        character.name = new_character['name']
        character.status = new_character['status']
        character.species = new_character['species']
        character.type = new_character['type']
        character.gender = new_character['gender']
        character.image = new_character['image']
        character.url = new_character['url']

        # take the origin_id from the origin_url
        if new_character['origin']['url'].split('/')[-1]:
            character.origin_id = new_character['origin']['url'].split('/')[-1]
        else:
            character.origin_id = None

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
        serialized_characters.append(serialized_character)

    return jsonify({
        "results": serialized_characters
    }), 200

def get_character_by_id(id):
    character = Character.query.filter_by(id=id).first()
    character_serialized = character.serialize()
    return jsonify({
        "results": character_serialized
    }), 200
