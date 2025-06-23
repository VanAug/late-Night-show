
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models import db

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episode_list = [
        {
            "id": ep.id,
            "date": ep.date,
            "number": ep.number
        } for ep in episodes
    ]
    return jsonify(episode_list), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    
    episode_data = {
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": []
    }
    
    for appearance in episode.appearances:
        episode_data["appearances"].append({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id
        })
    
    return jsonify(episode_data), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    # Delete related appearances first
    Appearance.query.filter_by(episode_id=id).delete()
    db.session.delete(episode)
    db.session.commit()

    return jsonify({"message": f"Episode {id} deleted"}), 200
