from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Post, Category, Image

class NewPostForm(FlaskForm):
    caption = StringField('caption', validators=[Length(min=2)])
    categories = StringField('categories', validators=[DataRequired()])
    images = FileField('images', validators=[DataRequired()])
