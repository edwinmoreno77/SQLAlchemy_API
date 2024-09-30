from flask import request, jsonify
from models import db, Episode
import json

def create_episodes():
    data = request.json

    for new_episode in data["episodes"]:
        episode = Episode()
        episode.name = new_episode['name']
        episode.air_date = new_episode['air_date']
        episode.episode = new_episode['episode']
        episode.url = new_episode['url']
        episode.characters = json.dumps(new_episode["characters"])

        db.session.add(episode)

    db.session.commit()

    return {
        "message": "Episodes created successfully",
    }, 201


def get_episodes():

    episodes = Episode.query.all()
    episodes_serialized = []

    for episode in episodes:
        episode_serialized = episode.serialize()
        episode_serialized["characters"] = json.loads(episode_serialized["characters"])

        episodes_serialized.append(episode_serialized)

    return jsonify({
        "results": episodes_serialized
    }), 201 