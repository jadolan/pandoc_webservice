from app import app
from app.forms import LoginForm, UploadForm
from flask import flash, render_template, request
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    # check if POST-request containing a file has been sent
    if form.validate_on_submit():
        filename = secure_filename(file.filename)
        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html', title='Pandoc Webservice', form=form)



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

# TODO: add login functionality