from flask import request, jsonify
from models import db, User, Favorites

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

    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Verify if favorite exists
    favorite = Favorites.query.filter_by(character_id=data['character_id'], user_id=user.id).first()

    if favorite:
        return jsonify({'message': 'Favorite already exists'}), 400

    # if not exists, add favorite
    favorite = Favorites(character_id=data['character_id'], user_id=user.id) 
    db.session.add(favorite)
    db.session.commit()  

    user.favorites.append(favorite)
    db.session.commit()  

    return jsonify({
        'message': 'Favorite added successfully',
    }), 200


def delete_favorite():

    data = request.json
    user = User.query.get(data['user_id'])

    if not user:
        return jsonify({'message': 'User not found'}), 404

    favorite = Favorites.query.filter_by(character_id=data['character_id'], user_id=user.id).first()

    if not favorite:
        return jsonify({'message': 'Favorite does not exist'}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Favorite deleted successfully'}), 200
