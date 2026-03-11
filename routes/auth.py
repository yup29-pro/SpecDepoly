from flask import Blueprint, redirect, url_for
from auth.google import login_with_google, google_callback

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login/google')
def login_google():
    return login_with_google()

@auth_blueprint.route('/login/google/callback')
def google_callback_route():
    return google_callback()
