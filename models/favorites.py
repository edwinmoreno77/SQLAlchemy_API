from . import db

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    character = db.relationship('Character', backref='favorites')

    def serialize(self):
        character_data = self.character.serialize() if self.character else None
        return {
            'id': self.id,
            'user_id': self.user_id,
            'character': character_data,
        }
