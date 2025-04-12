from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PrimeContractForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    contract_date = DateField('Contract Date', format='%Y-%m-%d')
    contract_value = StringField('Contract Value', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SubcontractForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    subcontract_date = DateField('Subcontract Date', format='%Y-%m-%d')
    subcontract_value = StringField('Subcontract Value', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProfessionalServiceAgreementForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    agreement_date = DateField('Agreement Date', format='%Y-%m-%d')
    agreement_value = StringField('Agreement Value', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LienWaiverForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    waiver_date = DateField('Waiver Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class CertificateOfInsuranceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    insurance_date = DateField('Insurance Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class LetterOfIntentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    intent_date = DateField('Intent Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')