from flask import request, jsonify
from models import db, Episode, Character

def create_episodes():
    data = request.json

    for new_episode in data["episodes"]:
        episode = Episode(
            name=new_episode['name'],
            air_date=new_episode['air_date'],
            episode=new_episode['episode'],
            url=new_episode['url']
        )

        db.session.add(episode)

        for character_url in new_episode['characters']:
                character_id = int(character_url.split('/')[-1])
                character = Character.query.get(character_id)
                if character:
                    episode.characters.append(character)
    db.session.commit()

    return {
        "message": "Episodes created successfully",
    }, 201


def get_episodes():

    episodes = Episode.query.all()
    episodes_serialized = []

    for episode in episodes:
        episode_serialized = episode.serialize()
        episodes_serialized.append(episode_serialized)

    return jsonify({
        "results": episodes_serialized
    }), 201 

def get_episode_by_id(id):

    episode = Episode.query.filter_by(id=id).first()
    episode_serialized = episode.serialize()

    return jsonify({
        "results": episode_serialized,
    }), 201