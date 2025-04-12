from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired

class ManualForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submission_date = DateField('Submission Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class WarrantyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    expiration_date = DateField('Expiration Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

class AtticStockForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    location = StringField('Location')
    submit = SubmitField('Submit')