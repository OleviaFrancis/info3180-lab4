from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import app

class UploadForm(FlaskForm):
    pictures = FileField('pictures', validators = [FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

