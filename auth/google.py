import os
import json
from flask import Flask, redirect, url_for, request, session
from google.oauth2 import id_token
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Google OAuth credentials
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'

# Google API client
def get_google_client():
    return build('oauth2', 'v2', developerKey=CLIENT_ID)

# Login with Google
def login_with_google():
    # Redirect to Google OAuth authorization page
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={url_for("google_callback", _external=True)}&scope=openid+email+profile'
    return redirect(auth_url)

# Google OAuth callback
def google_callback():
    # Get authorization code from Google
    code = request.args.get('code')
    # Exchange code for access token
    token_url = 'https://oauth2.googleapis.com/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'code': code, 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'redirect_uri': url_for('google_callback', _external=True), 'grant_type': 'authorization_code'}
    response = Request().post(token_url, headers=headers, data=data)
    # Get access token and user info
    access_token = response.json()['access_token']
    user_info_url = 'https://openidconnect.googleapis.com/v1/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = Request().get(user_info_url, headers=headers)
    user_info = response.json()
    # Store user info and access token in session
    session['user_info'] = user_info
    session['access_token'] = access_token
    return redirect(url_for('index'))
