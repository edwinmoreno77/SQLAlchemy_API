from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(20), nullable=False)
  favorites = db.relationship('Favorites', backref='user', lazy=True)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'last_name': self.last_name,
      'email': self.email,
      'favorites': [favorite.serialize() for favorite in self.favorites]
    }
  
class Favorites(db.Model):
  __tablename__ = "favorites"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
  episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=True)
  location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)

  def serialize(self):
    return {
      'id':self.id,
      'user_id': self.user_id,
      'character_id': self.character_id,
      'episode_id': self.episode_id,
      'location_id': self.location_id,
    }

character_episode = db.Table('character_episode',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
    db.Column('episode_id', db.Integer, db.ForeignKey('episode.id'), primary_key=True)
)

class Character(db.Model):
  __tablename__ = "character"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  status = db.Column(db.String(50), nullable=True)
  gender = db.Column(db.String(50), nullable=True)
  specie = db.Column(db.String(50), nullable=True)
  origin = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
  location = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
  episodes = db.relationship('Episode', secondary=character_episode, lazy='subquery',
                              backref=db.backref('characters', lazy=True))
  
  def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'status': self.status,
          'gender': self.gender,
          'specie': self.specie,
          'origin': self.origin,
          'location': self.location,
          'episodes': [episode.serialize() for episode in self.episodes] 
      }

  
class Episode(db.Model):
  __tablename__ = "episode"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, )
  air_date = db.Column(db.String, nullable=True)
  episode = db.Column(db.String, nullable=True)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'air_date':self.air_date,
      'episode':self.episode,
    }
  

class Location(db.Model):
  __tablename__ = "location"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, )
  location_type = db.Column(db.String, nullable=True)
  dimension = db.Column(db.String, nullable=True)
  url = db.Column(db.String, nullable=True)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'type':self.location_type,
      'dimension':self.dimension,
      'url': self.url,
    }

