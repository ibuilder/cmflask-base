from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class RFIForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submission_date = DateField('Submission Date', format='%Y-%m-%d')
    response_due_date = DateField('Response Due Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class SubmittalForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submission_date = DateField('Submission Date', format='%Y-%m-%d')
    approval_status = SelectField('Approval Status', choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class DrawingForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    drawing_date = DateField('Drawing Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class SpecificationForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    specification_date = DateField('Specification Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class FileExplorerForm(FlaskForm):
    file_name = StringField('File Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    upload_date = DateField('Upload Date', format='%Y-%m-%d')
    submit = SubmitField('Upload')

class PermittingForm(FlaskForm):
    permit_type = StringField('Permit Type', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submission_date = DateField('Submission Date', format='%Y-%m-%d')
    approval_status = SelectField('Approval Status', choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class MeetingAgendaForm(FlaskForm):
    agenda_title = StringField('Agenda Title', validators=[DataRequired()])
    agenda_items = TextAreaField('Agenda Items', validators=[DataRequired()])
    meeting_date = DateField('Meeting Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class TransmittalForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    transmittal_date = DateField('Transmittal Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')