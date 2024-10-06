from . import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(50))
    episode = db.Column(db.String(10))
    url = db.Column(db.String)
    characters = db.relationship('Character', secondary='character_episodes', backref='episodes_linked')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "characters": [character.url for character in self.characters], 
            'url': self.url
        }
