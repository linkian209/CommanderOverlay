from app.extensions import db, socketio
from app.models import Overlay
from flask import Blueprint, render_template, Response, request
from flask_login import login_required, current_user

overlay_bp = Blueprint('overlay', __name__, url_prefix='/overlay')

@overlay_bp.route('/manage', methods=['GET'])
@login_required
def manage() -> Response:
    return render_template('management.html.j2')

@overlay_bp.route('/manage', methods=['PUT'])
@login_required
def update():
    update_data = request.json
    current_user.overlay.update(update_data)
    socketio.emit('update', update_data, room=current_user.overlay.id)
    return Response(status=200)

@overlay_bp.route('/<overlay_id>', methods=['GET'])
def overlay(overlay_id: str) -> Response:
    overlay = db.get_or_404(Overlay, overlay_id)
    return render_template('overlay.html.j2', overlay=overlay)