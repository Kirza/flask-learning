from project import db
from project import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title_header = db.Column(db.String)
    title_long = db.Column(db.String)
    content = db.Column(db.String)
    tag = db.Column(db.String)
    creation_date = db.Column(db.String)
    image_link = db.Column(db.String)
    author_name_auto = db.Column(db.Integer, ForeignKey('users.id'))
    author_name_manual = db.Column(db.String)

    def __init__(self, title_header, title_long, content, tag, creation_date, image_link,  author_name_auto, author_name_manual):
        self.title_header = title_header
        self.title_long = title_long
        self.content = content
        self.tag = tag
        self.creation_date = creation_date
        self.image_link = image_link
        self.author_name_auto = author_name_auto
        self.author_name_manual = author_name_manual

    def __repr__(self):
        return '<title {}'.format(self.title_header)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name {}'.format(self.name)
