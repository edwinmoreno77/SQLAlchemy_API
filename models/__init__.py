from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User, user_character_favorites  
from .episode import Episode
from .character import Character, character_episodes
from .location import Location
