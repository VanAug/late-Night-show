from .appearance_controller import appearance_bp
from .auth_controller import auth_bp
from .episode_controller import episode_bp

all_blueprints = [auth_bp, episode_bp, appearance_bp]