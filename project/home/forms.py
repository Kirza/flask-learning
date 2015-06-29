from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(), Length(max=140)])

class BlogPostForm(Form):
    title_header = TextAreaField('Title header', validators=[DataRequired(), Length(max=80)])
    title_long = TextAreaField('Title long', validators=[Length(max=250)])
    content = TextAreaField('Main content', validators=[DataRequired(), Length(max=25000)])
    tag = TextAreaField('Tags', validators=[Length(max=25)])
    image_link = TextAreaField('Image', validators=[DataRequired(), Length(max=100)])
    author_name_manual = TextAreaField('Only fill if author name dont match your username', validators=[Length(max=25)])
