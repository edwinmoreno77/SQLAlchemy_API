from flask import request, jsonify
from models import db, User, Character

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

def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    return {
        "status": "success",
        "data": user.serialize()
    }, 200

def get_users():
    users = User.query.all()
    users_serialized = [user.serialize() for user in users]

    return jsonify({
        "status": "success",
        "data": users_serialized
    }), 200


def add_favorite():
    data = request.json

    user = User.query.get(data['user_id'])
    character = Character.query.get(data['character_id'])

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if character in user.favorite_characters:
        return jsonify({'message': 'Favorite already exists'}), 400

    user.favorite_characters.append(character)
    db.session.commit()  

    return jsonify({
        'message': 'Favorite added successfully',
    }), 200


def delete_favorite():

    data = request.json
    user = User.query.get(data['user_id'])
    character = Character.query.get(data['character_id'])

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if character not in user.favorite_characters:
        return jsonify({'message': 'Favorite does not exist'}), 404
    
    user.favorite_characters.remove(character)
    db.session.commit()

    return jsonify({'message': 'Favorite deleted successfully'}), 200
