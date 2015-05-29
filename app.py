#################
#### imports ####
#################

from flask import Flask, flash, redirect, session, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import os

################
#### config ####
################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)

##########################
#### helper functions ####
##########################


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


################
#### routes ####
################

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template

<<<<<<< HEAD
=======
@app.route('/blog')
@login_required
def blog():
    return render_template('blog.html')  # render a template

@app.route('/post')
def post():
    return render_template('post.html')  # render a template

@app.route('/blog2')
@login_required
def blog2():
    return render_template('blog2.html')  # render a template

@app.route('/preview')
@login_required
def preview():
    return render_template('preview.html')  # render a template

>>>>>>> c3647af232ac5b6042d145d235160210940edd68

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


####################
#### run server ####
####################

if __name__ == '__main__':
    app.run()
