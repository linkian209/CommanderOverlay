from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, join_room, leave_room
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO()
cors = CORS()

@socketio.on('join')
def on_connect(data):
    join_room(data)

@socketio.on('leave')
def on_disconnect(data):
    leave_room(data)