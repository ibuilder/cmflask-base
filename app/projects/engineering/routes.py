from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import engineering_bp
from .forms import RFIForm, SubmittalForm, DrawingForm, SpecificationForm, FileExplorerForm, PermitForm, MeetingAgendaForm, TransmittalForm
from app.models.engineering import RFI, Submittal, Drawing, Specification, Permit, MeetingAgenda, Transmittal
from app.models.project import Project
from app.extensions import db
from datetime import datetime

@engineering_bp.route('/rfis')
@login_required
def rfis():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    rfis = RFI.query.filter_by(project_id=project_id).order_by(RFI.date_submitted.desc()).all()
    return render_template('projects/engineering/rfis.html', project=project, rfis=rfis)

@engineering_bp.route('/rfis/create', methods=['GET', 'POST'])
@login_required
def create_rfi():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = RFIForm()
    if form.validate_on_submit():
        rfi = RFI(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            date_submitted=datetime.now(),
            submitted_by=current_user.id
        )
        db.session.add(rfi)
        db.session.commit()
        flash('RFI created successfully!', 'success')
        return redirect(url_for('projects.engineering.rfis', project_id=project_id))
    return render_template('projects/engineering/create_rfi.html', project=project, form=form)

@engineering_bp.route('/submittals')
@login_required
def submittals():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    submittals = Submittal.query.filter_by(project_id=project_id).order_by(Submittal.date_submitted.desc()).all()
    return render_template('projects/engineering/submittals.html', project=project, submittals=submittals)

@engineering_bp.route('/submittals/create', methods=['GET', 'POST'])
@login_required
def create_submittal():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = SubmittalForm()
    if form.validate_on_submit():
        submittal = Submittal(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            date_submitted=datetime.now(),
            submitted_by=current_user.id
        )
        db.session.add(submittal)
        db.session.commit()
        flash('Submittal created successfully!', 'success')
        return redirect(url_for('projects.engineering.submittals', project_id=project_id))
    return render_template('projects/engineering/create_submittal.html', project=project, form=form)

@engineering_bp.route('/drawings')
@login_required
def drawings():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    drawings = Drawing.query.filter_by(project_id=project_id).order_by(Drawing.date_uploaded.desc()).all()
    return render_template('projects/engineering/drawings.html', project=project, drawings=drawings)

@engineering_bp.route('/drawings/create', methods=['GET', 'POST'])
@login_required
def create_drawing():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = DrawingForm()
    if form.validate_on_submit():
        drawing = Drawing(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            date_uploaded=datetime.now(),
            uploaded_by=current_user.id
        )
        db.session.add(drawing)
        db.session.commit()
        flash('Drawing uploaded successfully!', 'success')
        return redirect(url_for('projects.engineering.drawings', project_id=project_id))
    return render_template('projects/engineering/create_drawing.html', project=project, form=form)

@engineering_bp.route('/specifications')
@login_required
def specifications():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    specifications = Specification.query.filter_by(project_id=project_id).order_by(Specification.date_uploaded.desc()).all()
    return render_template('projects/engineering/specifications.html', project=project, specifications=specifications)

@engineering_bp.route('/specifications/create', methods=['GET', 'POST'])
@login_required
def create_specification():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = SpecificationForm()
    if form.validate_on_submit():
        specification = Specification(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            date_uploaded=datetime.now(),
            uploaded_by=current_user.id
        )
        db.session.add(specification)
        db.session.commit()
        flash('Specification uploaded successfully!', 'success')
        return redirect(url_for('projects.engineering.specifications', project_id=project_id))
    return render_template('projects/engineering/create_specification.html', project=project, form=form)

@engineering_bp.route('/permits')
@login_required
def permits():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    permits = Permit.query.filter_by(project_id=project_id).order_by(Permit.date_applied.desc()).all()
    return render_template('projects/engineering/permits.html', project=project, permits=permits)

@engineering_bp.route('/permits/create', methods=['GET', 'POST'])
@login_required
def create_permit():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = PermitForm()
    if form.validate_on_submit():
        permit = Permit(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            date_applied=datetime.now(),
            applied_by=current_user.id
        )
        db.session.add(permit)
        db.session.commit()
        flash('Permit applied successfully!', 'success')
        return redirect(url_for('projects.engineering.permits', project_id=project_id))
    return render_template('projects/engineering/create_permit.html', project=project, form=form)

@engineering_bp.route('/meetings')
@login_required
def meetings():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    meetings = MeetingAgenda.query.filter_by(project_id=project_id).order_by(MeetingAgenda.date_meeting.desc()).all()
    return render_template('projects/engineering/meetings.html', project=project, meetings=meetings)

@engineering_bp.route('/meetings/create', methods=['GET', 'POST'])
@login_required
def create_meeting():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = MeetingAgendaForm()
    if form.validate_on_submit():
        meeting = MeetingAgenda(
            project_id=project_id,
            title=form.title.data,
            date_meeting=form.date_meeting.data,
            time_meeting=form.time_meeting.data,
            agenda=form.agenda.data,
            created_by=current_user.id
        )
        db.session.add(meeting)
        db.session.commit()
        flash('Meeting agenda created successfully!', 'success')
        return redirect(url_for('projects.engineering.meetings', project_id=project_id))
    return render_template('projects/engineering/create_meeting.html', project=project, form=form)

@engineering_bp.route('/transmittals')
@login_required
def transmittals():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    transmittals = Transmittal.query.filter_by(project_id=project_id).order_by(Transmittal.date_sent.desc()).all()
    return render_template('projects/engineering/transmittals.html', project=project, transmittals=transmittals)

@engineering_bp.route('/transmittals/create', methods=['GET', 'POST'])
@login_required
def create_transmittal():
    project_id = request.args.get('project_id', type=int)
    project = Project.query.get_or_404(project_id)
    form = TransmittalForm()
    if form.validate_on_submit():
        transmittal = Transmittal(
            project_id=project_id,
            title=form.title.data,
            description=form.description.data,
            date_sent=datetime.now(),
            sent_by=current_user.id
        )
        db.session.add(transmittal)
        db.session.commit()
        flash('Transmittal sent successfully!', 'success')
        return redirect(url_for('projects.engineering.transmittals', project_id=project_id))
    return render_template('projects/engineering/create_transmittal.html', project=project, form=form)