from . import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(50))
    episode = db.Column(db.String(10))
    characters = db.Column(db.Text) 
    url = db.Column(db.String)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode,
            "characters": self.characters,
            'url': self.url
        }
