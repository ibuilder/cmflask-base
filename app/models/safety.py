from datetime import datetime
from app.extensions import db

class SafetyObservation(db.Model):
    __tablename__ = 'safety_observations'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    observation_date = db.Column(db.Date, default=datetime.utcnow)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='open')
    observed_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='safety_observations')
    observed_user = db.relationship('User', foreign_keys=[observed_by])
    created_user = db.relationship('User', foreign_keys=[created_by])

class IncidentReport(db.Model):
    __tablename__ = 'incident_reports'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    incident_date = db.Column(db.Date, nullable=False)
    incident_time = db.Column(db.String(50))
    location = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    reported_by_name = db.Column(db.String(255))
    reported_by_title = db.Column(db.String(255))
    witness_names = db.Column(db.String(255))
    root_cause = db.Column(db.Text)
    corrective_actions = db.Column(db.Text)
    is_osha_recordable = db.Column(db.Boolean, default=False)
    is_lost_time = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship('Project', back_populates='incident_reports')
    created_user = db.relationship('User', foreign_keys=[created_by])