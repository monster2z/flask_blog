from flask_wtf import FlaskForm
from flask import render_template, render_template, redirect,url_for
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Optional
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from . import main
import os

class PhotoForm(FlaskForm) :
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')

class NameForm(FlaskForm) :
    name = StringField('What is your name?', validators=[Required()])
    # contents = TextAreaField('type contents', validators = [Optional()])
    submit = SubmitField('Submit')

@main.route('/upload', methods=['GET','POST'])
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(os.path.dirname(__file__),'static','photos',filename))
        return redirect(url_for('index'))
    return render_template('upload.html',form=form)