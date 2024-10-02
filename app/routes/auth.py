from app.extensions import db, login_manager
from app.models import User, Overlay
from flask import Blueprint, request, jsonify, redirect, url_for, session, current_app, Response
from flask_login import login_user, logout_user
from requests_oauthlib import OAuth2Session
import uuid


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

DISCORD_API_BASE_URL = "https://discord.com/api"
DISCORD_AUTHORIZATION_BASE_URL = f"{DISCORD_API_BASE_URL}/oauth2/authorize"
DISCORD_TOKEN_URL = f"{DISCORD_API_BASE_URL}/oauth2/token"

@login_manager.user_loader
def load_user(user_id: str) -> User:
    return db.session.query(User).get(int(user_id))

def token_updater(token: dict) -> None:
    session["oauth2_token"] = token

def make_session(token=None, state=None, scope=None) -> OAuth2Session:
    return OAuth2Session(
        current_app.config.get("DISCORD_CLIENT_ID"),
        token=token,
        state=state,
        scope=scope,
        redirect_uri=current_app.config.get("DISCORD_REDIRECT_URI"),
        auto_refresh_kwargs={
            'client_id': current_app.config.get("DISCORD_CLIENT_ID"),
            'client_secret': current_app.config.get("DISCORD_CLIENT_SECRET"),
        },
        auto_refresh_url=current_app.config.get(DISCORD_TOKEN_URL),
        token_updater=token_updater
    )

@auth_bp.route('/login', methods=['GET'])
def login() -> Response:
    discord = make_session(scope=['identify'])
    authorization_url, state = discord.authorization_url(DISCORD_AUTHORIZATION_BASE_URL)
    session['oauth_state'] = state
    return redirect(authorization_url)

@auth_bp.route('/callback', methods=['GET'])
def callback() -> Response:
    discord = make_session(state=session['oauth_state'])
    token = discord.fetch_token(
        DISCORD_TOKEN_URL,
        client_secret=current_app.config.get("DISCORD_CLIENT_SECRET"),
        authorization_response=request.url
    )

    if 'access_token' not in token:
        return jsonify({"error": "Failed to obtain access token"}), 400

    token_updater(token)

    discord = make_session(token=token)
    user_info_url = f"{DISCORD_API_BASE_URL}/users/@me"
    user_info_response = discord.get(user_info_url)
    user_info = user_info_response.json()

    user = load_user(user_info['id'])
    if(user is None):
        user = User(id=user_info['id'], username=user_info['username'])
        overlay = Overlay(id=uuid.uuid4().hex, user_id=user.id)
        user.overlay = overlay
        db.session.add(user)
        db.session.add(overlay)
        db.session.commit()
        db.session.refresh(user)
    login_user(user)

    return redirect(url_for('overlay.manage'))

@auth_bp.route('/logout', methods=['GET'])
def logout() -> Response:
    session.clear()
    logout_user()
    return redirect(url_for('index'))