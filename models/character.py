from . import db

character_episodes = db.Table('character_episodes',
        db.Column('character_id', db.Integer, db.ForeignKey('characters.id'), primary_key=True),
        db.Column('episodes_id', db.Integer, db.ForeignKey('episodes.id'), primary_key=True)
)

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20))
    species = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'))  
    origin = db.relationship('Location', foreign_keys=[origin_id], backref='origin_character') 
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location = db.relationship('Location', foreign_keys=[location_id], backref='location_character') 
    image = db.Column(db.String(255))
    episodes = db.relationship('Episode', secondary='character_episodes', backref='characters_linked')  
    url = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            "origin": {
                "name": self.origin.name, 
                "url": self.origin.url
            } 
            if self.origin else None,
            "location": {
                "name": self.location.name, 
                "url": self.location.url
            } 
            if self.location else None,
            "image": self.image,
            "episodes": [episode.url for episode in self.episodes],
            "url": self.url
        }
