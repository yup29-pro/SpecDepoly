import pytest
from unittest.mock import patch, Mock
from flask import Flask
from auth.google import login_with_google, google_callback, get_google_client
from routes.auth import auth_blueprint
from config import CLIENT_ID, CLIENT_SECRET, SECRET_KEY

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(auth_blueprint)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_login_with_google(client):
    with patch('auth.google.url_for') as mock_url_for:
        mock_url_for.return_value = 'https://example.com/callback'
        response = client.get('/login/google')
        assert response.status_code == 302
        assert 'https://accounts.google.com/o/oauth2/v2/auth' in response.location

def test_google_callback(client):
    with patch('auth.google.Request') as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {'access_token': 'token'}
        mock_request.return_value.post.return_value = mock_response
        response = client.get('/login/google/callback', query_string={'code': 'code'})
        assert response.status_code == 302
        assert 'http://localhost/' in response.location

def test_get_google_client():
    client = get_google_client()
    assert client

def test_login_with_google_error(client):
    with patch('auth.google.Request') as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {'error': 'error'}
        mock_request.return_value.post.return_value = mock_response
        response = client.get('/login/google/callback', query_string={'code': 'code'})
        assert response.status_code == 500

def test_google_callback_error(client):
    with patch('auth.google.Request') as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {'error': 'error'}
        mock_request.return_value.get.return_value = mock_response
        response = client.get('/login/google/callback', query_string={'code': 'code'})
        assert response.status_code == 500

def test_get_google_client_error():
    with patch('googleapiclient.discovery.build') as mock_build:
        mock_build.side_effect = Exception('error')
        with pytest.raises(Exception):
            get_google_client()