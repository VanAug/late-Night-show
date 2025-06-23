
from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest', __name__)

# List all guests
@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        "id": guest.id,
        "name": guest.name,
        "ingredients": guest.occupation
    } for guest in guests]), 200
