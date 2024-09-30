from flask import request, jsonify
from models import db, User

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
