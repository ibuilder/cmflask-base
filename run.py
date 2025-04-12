from flask import Flask
from app.extensions import db
from app.models import User, Project
from app.projects.safety import safety_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(safety_bp, url_prefix='/safety')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)