from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import safety_bp
from .forms import SafetyObservationForm, IncidentReportForm
from app.models.safety import SafetyObservation, IncidentReport
from app.models.project import Project
from app.extensions import db
from app.utils.access_control import role_required
from datetime import datetime

@safety_bp.route('/dashboard')
@login_required
def dashboard():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    # Logic to gather safety metrics and recent incidents
    return render_template('projects/safety/dashboard.html', project=project)

@safety_bp.route('/observations')
@login_required
def observations():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    observations = SafetyObservation.query.filter_by(project_id=project_id).order_by(SafetyObservation.observation_date.desc()).all()
    return render_template('projects/safety/observations/list.html', project=project, observations=observations)

@safety_bp.route('/observations/create', methods=['GET', 'POST'])
@login_required
def create_observation():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = SafetyObservationForm()
    if form.validate_on_submit():
        observation = SafetyObservation(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            observation_date=form.observation_date.data or datetime.now().date(),
            location=form.location.data,
            category=form.category.data,
            severity=form.severity.data,
            status='open',
            observed_by=current_user.id,
            created_by=current_user.id
        )
        db.session.add(observation)
        db.session.commit()
        flash('Safety observation recorded successfully!', 'success')
        return redirect(url_for('projects.safety.observations', project_id=project_id))
    return render_template('projects/safety/observations/create.html', project=project, form=form)

@safety_bp.route('/observations/<int:id>')
@login_required
def view_observation(id):
    observation = SafetyObservation.query.get_or_404(id)
    project = Project.query.get_or_404(observation.project_id)
    return render_template('projects/safety/observations/view.html', project=project, observation=observation)

@safety_bp.route('/incidents')
@login_required
def incidents():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    incidents = IncidentReport.query.filter_by(project_id=project_id).order_by(IncidentReport.incident_date.desc()).all()
    return render_template('projects/safety/incidents/list.html', project=project, incidents=incidents)

@safety_bp.route('/incidents/create', methods=['GET', 'POST'])
@login_required
@role_required(['Admin', 'Owner', 'Owners Representative', 'General Contractor'])
def create_incident():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = IncidentReportForm()
    if form.validate_on_submit():
        incident = IncidentReport(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            incident_date=form.incident_date.data,
            incident_time=form.incident_time.data,
            location=form.location.data,
            type=form.type.data,
            severity=form.severity.data,
            reported_by_name=form.reported_by_name.data,
            reported_by_title=form.reported_by_title.data,
            witness_names=form.witness_names.data,
            root_cause=form.root_cause.data,
            corrective_actions=form.corrective_actions.data,
            is_osha_recordable=form.is_osha_recordable.data,
            is_lost_time=form.is_lost_time.data,
            created_by=current_user.id
        )
        db.session.add(incident)
        db.session.commit()
        flash('Incident report created successfully!', 'success')
        return redirect(url_for('projects.safety.incidents', project_id=project_id))
    return render_template('projects/safety/incidents/create.html', project=project, form=form)