import pytest
from flask import url_for
from app import create_app, db
from app.models.user import User

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_login(client):
    response = client.post(url_for('auth.login'), data={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data

def test_register(client):
    response = client.post(url_for('auth.register'), data={
        'username': 'newuser',
        'password': 'newpassword',
        'confirm_password': 'newpassword'
    })
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_login_invalid(client):
    response = client.post(url_for('auth.login'), data={
        'username': 'invaliduser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_logout(client):
    client.post(url_for('auth.login'), data={
        'username': 'testuser',
        'password': 'testpassword'
    })
    response = client.get(url_for('auth.logout'))
    assert response.status_code == 302
    assert b'You have been logged out' in response.data