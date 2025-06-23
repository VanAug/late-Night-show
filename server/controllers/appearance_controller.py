from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models import db
from server.models.guest import Guest
from server.models.episode import Episode

appearance_bp = Blueprint('appearance', __name__)

# POST /appearances - create new appearance (auth required)
@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        return jsonify({"error": "Missing required fields"}), 400

    # Validate guest and episode existence
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return jsonify({"error": "Invalid guest or episode ID"}), 404

    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict()), 201
