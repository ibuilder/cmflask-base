from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class QualifiedBiddersForm(FlaskForm):
    name = StringField('Bidder Name', validators=[DataRequired()])
    contact_info = StringField('Contact Information', validators=[DataRequired()])
    qualifications = TextAreaField('Qualifications', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BidPackagesForm(FlaskForm):
    package_name = StringField('Package Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submission_deadline = DateField('Submission Deadline', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BidManualForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')