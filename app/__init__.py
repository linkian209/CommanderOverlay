from app.extensions import db, migrate, login_manager, socketio
from app.routes.auth import auth_bp
from app.routes.overlay import overlay_bp
from flask import Flask, redirect, url_for, render_template
from flask_login import current_user
from werkzeug.middleware.proxy_fix import ProxyFix
import json
import os

def error_handler(error):
    return render_template("error.html.j2", error=error)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configuration settings
    # First from config file
    app.config.from_file("config.json", load=json.load)

    # Next from environment variable
    app.config.from_prefixed_env()

    if(app.config.get("OAUTHLIB_INSECURE_TRANSPORT")):
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    if(app.config.get("DEBUG") == False):
        app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_for=1, x_port=1, x_prefix=1)

    app.register_error_handler(404, error_handler)
    app.register_error_handler(500, error_handler)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)

    # Make sure flask migrate knows about them
    from app.models import User, Overlay

    app.register_blueprint(auth_bp)
    app.register_blueprint(overlay_bp)

    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("overlay.manage"))
        return render_template("index.html.j2")

    return app