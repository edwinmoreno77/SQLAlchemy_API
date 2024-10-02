from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .episode import Episode
from .character import Character
from .location import Location
from .favorites import Favorites
