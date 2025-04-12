from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import reports_bp
from app.models.safety import SafetyObservation, IncidentReport
from app.models.project import Project
from app.extensions import db

@reports_bp.route('/safety/observations')
@login_required
def safety_observations():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    observations = SafetyObservation.query.filter_by(project_id=project_id).order_by(SafetyObservation.observation_date.desc()).all()
    return render_template('reports/safety_observations.html', project=project, observations=observations)

@reports_bp.route('/safety/incidents')
@login_required
def safety_incidents():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    incidents = IncidentReport.query.filter_by(project_id=project_id).order_by(IncidentReport.incident_date.desc()).all()
    return render_template('reports/safety_incidents.html', project=project, incidents=incidents)

@reports_bp.route('/safety/report/<int:id>')
@login_required
def safety_report(id):
    observation = SafetyObservation.query.get_or_404(id)
    return render_template('reports/safety_report.html', observation=observation)

@reports_bp.route('/safety/report/incident/<int:id>')
@login_required
def safety_incident_report(id):
    incident = IncidentReport.query.get_or_404(id)
    return render_template('reports/safety_incident_report.html', incident=incident)