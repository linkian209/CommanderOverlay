from app import create_app
from app.extensions import socketio
from werkzeug.middleware.proxy_fix import ProxyFix

if __name__ == "__main__":
    app = create_app()
    if(app.config.get("DEBUG") == False):
        app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_for=1, x_port=1, x_prefix=1)
    socketio.run(app)