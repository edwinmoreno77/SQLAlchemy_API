from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Specie
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/createUser', methods=['POST'])
def create():
  data = request.json
  user = User()

  print(data['name'])
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


@app.route("/getUSer", methods=['GET'])
def get_user():
  user = User.query.all()
  user_serializados = list(map(lambda usuario: usuario.serialize(), user))

  return jsonify({
    "status": "success",
    "data": user_serializados
  }), 200


# specie

@app.route('/createSpecie', methods=['POST'])
def create_specie():
  data = request.json
  specie = Specie()

  print(data['name'])
  specie.name = data['name']
 
  db.session.add(specie)
  db.session.commit()

  return {
    "message": "Specie created successfully",
  }, 201


if __name__ == '__main__': 
    app.run('localhost', port=3000, debug=True)