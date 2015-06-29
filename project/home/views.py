#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from forms import MessageForm, BlogPostForm
from project import db
from project.models import BlogPost

import datetime

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


@home_blueprint.route('/preview')
@login_required
def preview():
    return render_template('preview.html')  # render a template


@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def blog():
    posts = db.session.query(BlogPost).all()
    return render_template('blog.html', posts=posts)  # render a template


@home_blueprint.route('/<int:post_id>')
@login_required
def post_generate(post_id):
    post = db.session.query(BlogPost).filter(BlogPost.id == post_id).first()
    content = post.content
    content = content.replace("\r", " </p> ", 40)
    content = content.replace("\n", " <p> ", 40)
    return render_template('post_dyn.html', post=post, content=content)

@home_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    error = None
    date = datetime.datetime.now()
    form = BlogPostForm(request.form)
    if form.validate_on_submit():
        new_post = BlogPost(
            form.title_header.data,
            form.title_long.data,
            form.content.data,
            form.tag.data,
            date,
            form.image_link.data,
            current_user.id,
            form.author_name_manual.data
        )
        db.session.add(new_post)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.create'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'create.html', posts=posts, form=form, error=error)
