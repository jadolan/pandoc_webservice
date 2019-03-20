from app import app
from app.forms import LoginForm, UploadForm
from app.convert import callPandoc
from flask import flash, render_template, request, make_response
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('upload.html', form=UploadForm())


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    # check if POST-request containing a file has been sent
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        converted_file = callPandoc(filepath)
        try:
            response = make_response(os.path.splitext(filepath)[0] + '.pdf')
            response.headers['Content-Disposition'] = 'attachment; filename=' + os.path.splitext(filename)[0] + ".pdf"
            response.headers['Cache-Control'] = 'must-revalidate'
            response.headers['Content-type'] = 'application/pdf'
        except Exception as e:
            print(str(e))
        return response


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

# TODO: add login functionality
