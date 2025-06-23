
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models import db

episode_bp = Blueprint('episode', __name__)

# GET all episodes
@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episode_list = [ep.to_dict() for ep in episodes]
    return jsonify(episode_list), 200

# GET single episode with appearances
@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict_with_appearances()), 200

# DELETE episode and related appearances
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
