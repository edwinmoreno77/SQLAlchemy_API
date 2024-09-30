from . import db

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20))
    species = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    origin = db.Column(db.Text)  
    location = db.Column(db.Text)  
    image = db.Column(db.String(255))
    episodes = db.Column(db.Text)  
    url = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image,
            "episodes": self.episodes,
            "url": self.url
        }
