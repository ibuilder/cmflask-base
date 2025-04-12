import pytest
from app import create_app, db
from app.models.project import Project
from app.models.safety import SafetyObservation, IncidentReport
from flask_login import current_user

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    project = Project(name='Test Project')
    db.session.add(project)
    db.session.commit()
    yield db  # This allows us to use the database in tests
    db.session.remove()

def test_create_safety_observation(client, init_database):
    response = client.post('/safety/observations/create', data={
        'title': 'Test Observation',
        'description': 'This is a test observation.',
        'observation_date': '2023-10-01',
        'location': 'Site A',
        'category': 'hazard',
        'severity': 'medium'
    })
    assert response.status_code == 302  # Check for redirect after successful creation
    observation = SafetyObservation.query.filter_by(title='Test Observation').first()
    assert observation is not None

def test_create_incident_report(client, init_database):
    response = client.post('/safety/incidents/create', data={
        'title': 'Test Incident',
        'description': 'This is a test incident report.',
        'incident_date': '2023-10-01',
        'incident_time': '10:00 AM',
        'location': 'Site B',
        'type': 'accident',
        'severity': 'high',
        'reported_by_name': 'John Doe',
        'reported_by_title': 'Foreman',
        'witness_names': 'Jane Smith',
        'root_cause': 'Equipment failure',
        'corrective_actions': 'Replace equipment',
        'is_osha_recordable': 'yes',
        'is_lost_time': 'no'
    })
    assert response.status_code == 302  # Check for redirect after successful creation
    incident = IncidentReport.query.filter_by(title='Test Incident').first()
    assert incident is not None

def test_list_safety_observations(client, init_database):
    response = client.get('/safety/observations')
    assert response.status_code == 200
    assert b'Test Observation' in response.data

def test_list_incidents(client, init_database):
    response = client.get('/safety/incidents')
    assert response.status_code == 200
    assert b'Test Incident' in response.data