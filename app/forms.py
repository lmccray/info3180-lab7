from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Length, DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=250)])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only images allowed!')])

