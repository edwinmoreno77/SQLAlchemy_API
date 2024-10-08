from . import db

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100))
    dimension = db.Column(db.String(100))
    residents = db.relationship('Character', backref='location_linked', foreign_keys='Character.location_id')
    url = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
            "residents": [ resident.url for resident in self.residents],
            "url": self.url
        }
