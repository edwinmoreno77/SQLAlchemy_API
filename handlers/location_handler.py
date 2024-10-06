from flask import request, jsonify
from models import db, Location, Character

def create_locations():
    data = request.json

    for new_location in data["locations"]:
        location = Location()
        location.name = new_location['name']
        location.type = new_location['type']
        location.dimension = new_location['dimension']
        location.url = new_location['url']
        db.session.add(location)

        for character_url in new_location['residents']:
            character_id = int(character_url.split('/')[-1])
            character = Character.query.get(character_id)
            if character:
                    location.residents.append(character)
    db.session.commit()

    return {
        "message": "Locations created successfully",
    }, 201

def get_locations():
    locations = Location.query.all()
    serialized_locations = []

    for location in locations:
        serialized_location = location.serialize()
        serialized_locations.append(serialized_location)

    return jsonify({
        "results": serialized_locations
    }), 200


def get_location_by_id(id):
    
    location = Location.query.filter_by(id=id).first()
    serialized_location = location.serialize()

    return jsonify({
        "results": serialized_location
    }), 200