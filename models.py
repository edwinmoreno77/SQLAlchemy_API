from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(16), nullable=False)
  favorites = db.relationship('Favorites', backref='user', lazy=True)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'last_name': self.last_name,
      'email': self.email,
      'favorites': [fav.serialize() for fav in self.favorites]
    }
  
class Favorites(db.Model):
  __tablename__ = "favorites"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
  episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
  location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)

  def serialize(self):
    return {
      'id':self.id,
      'user_id': self.user_id,
      'character_id': self.character_id,
      'episode_id': self.episode_id,
      'location_id': self.location_id,
    }

class Character(db.Model):
  __tablename__ = "character"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, )
  status = db.Column(db.String(50), nullable=False)
  gender = db.Column(db.String(50), nullable=False, )
  location = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False )

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'status': self.status,
      'gender': self.gender,
      'location':self.location,
    }
  
class location(db.Model):
  __tablename__ = "location"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, )
  url = db.Column(db.String(50), nullable=False)

def serialize(self):
  return {
    'id': self.id,
    'name': self.name,
    'url': self.url,
  }

class Specie(db.Model):
  __tablename__ = "specie"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, )

def serialize(self):
  return {
    'id': self.id,
    'name': self.name,
  }

class Episode(db.Model):
  __tablename__ = "episode"
  id = db.Column(db.Integer, primary_key=True)
  number = db.Column(db.Integer, nullable=False, )

def serialize(self):
  return {
    'id': self.id,
    'number': self.number,
  }