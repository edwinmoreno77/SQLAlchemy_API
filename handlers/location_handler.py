from flask import request, jsonify
from models import db, Location
import json

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
