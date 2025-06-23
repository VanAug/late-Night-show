
from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest', __name__)

# List all guests
@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guest_list = [guest.to_dict() for guest in guests]
    return jsonify(guest_list), 200
