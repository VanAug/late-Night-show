from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager 
from server.models import db
from server.config import Config
from server.controllers import all_blueprints

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

db.init_app(app)
migration = Migrate(app, db)

for bp in all_blueprints:
    app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)