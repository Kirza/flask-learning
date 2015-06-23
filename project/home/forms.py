from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(), Length(max=140)])

class BlogPostForm(Form):
    title_header = TextAreaField('Title header', validators=[DataRequired(), Length(max=40)])
    title_long = TextAreaField('Title long', validators=[DataRequired(), Length(max=60)])
    content = TextAreaField('Main content', validators=[DataRequired(), Length(max=1500)])
    tag = TextAreaField('Main content', validators=[Length(max=25)])
