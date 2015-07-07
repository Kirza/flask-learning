#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user
from werkzeug import secure_filename
from forms import MessageForm, BlogPostForm, PhotoForm
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
    upload = UploadForm(request.form)
    if form.validate_on_submit() and upload.validate_on_submit():
        filename = secure_filename(upload.image.data.filename)
        upload.image.data.save('static/images/source' + filename)
        new_post = BlogPost(
            form.title_header.data,
            form.title_long.data,
            form.content.data,
            form.tag.data,
            date,
            'static/images/source' + filename,
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
            'create.html', posts=posts, form=form, error=error, upload=upload)

@home_blueprint.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('project/static/images/' + filename)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)
    # form = PhotoForm(request.form)
    # if form.validate_on_submit():
    #     filename = secure_filename(form.image.name)
    #     form.image.save('static/images/source' + '1')
    #     flash('New image was successfully posted. Thanks.')
    #     print 'images saved to', 'static/images/source' + filename
    #     return redirect(url_for('home.upload'))
    # else:
    #     filename = None
    #     return render_template(
    #         'upload.html', form=form, filename=filename)
