import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    from puzzle import run_app
    # apply the blueprints to the app
    app.register_blueprint(run_app.ra)
    return app
