#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from forms import MessageForm
from project import db
from project.models import BlogPost

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/preview')
@login_required
def preview():
    return render_template('preview.html')  # render a template


@home_blueprint.route('/blog')
@login_required
def blog():
    return render_template('blog.html')  # render a template


@home_blueprint.route('/post')
@login_required
def post():
    return render_template('post.html')  # render a template
