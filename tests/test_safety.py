import pytest
from app import create_app, db
from app.models.safety import SafetyObservation, IncidentReport
from app.models.project import Project
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
def login(client):
    # Assuming you have a user with username 'testuser' and password 'password'
    client.post('/login', data={'username': 'testuser', 'password': 'password'})

@pytest.fixture
def project():
    new_project = Project(name='Test Project')
    db.session.add(new_project)
    db.session.commit()
    return new_project

def test_create_safety_observation(client, login, project):
    response = client.post(f'/projects/safety/observations/create?project_id={project.id}', data={
        'title': 'Test Observation',
        'description': 'This is a test observation.',
        'observation_date': '2023-10-01',
        'location': 'Site A',
        'category': 'hazard',
        'severity': 'medium'
    })
    assert response.status_code == 302  # Redirect after successful creation
    assert SafetyObservation.query.count() == 1

def test_list_safety_observations(client, login, project):
    client.post(f'/projects/safety/observations/create?project_id={project.id}', data={
        'title': 'Test Observation',
        'description': 'This is a test observation.',
        'observation_date': '2023-10-01',
        'location': 'Site A',
        'category': 'hazard',
        'severity': 'medium'
    })
    response = client.get(f'/projects/safety/observations?project_id={project.id}')
    assert b'Test Observation' in response.data

def test_create_incident_report(client, login, project):
    response = client.post(f'/projects/safety/incidents/create?project_id={project.id}', data={
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
    assert response.status_code == 302  # Redirect after successful creation
    assert IncidentReport.query.count() == 1

def test_list_incident_reports(client, login, project):
    client.post(f'/projects/safety/incidents/create?project_id={project.id}', data={
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
    response = client.get(f'/projects/safety/incidents?project_id={project.id}')
    assert b'Test Incident' in response.data