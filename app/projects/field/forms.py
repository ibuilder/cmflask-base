from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class DailyReportForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    weather = StringField('Weather', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit')

class PhotoUploadForm(FlaskForm):
    description = StringField('Description')
    photo = StringField('Photo URL', validators=[DataRequired()])
    submit = SubmitField('Upload')

class ScheduleForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    task = StringField('Task', validators=[DataRequired()])
    responsible_person = StringField('Responsible Person')
    submit = SubmitField('Add Task')

class ChecklistForm(FlaskForm):
    item = StringField('Checklist Item', validators=[DataRequired()])
    completed = SelectField('Completed', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    submit = SubmitField('Add Item')

class PunchlistForm(FlaskForm):
    issue = StringField('Issue', validators=[DataRequired()])
    resolution = TextAreaField('Resolution')
    submit = SubmitField('Add Issue')

class PullPlanningForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    duration = StringField('Duration')
    submit = SubmitField('Add Task')