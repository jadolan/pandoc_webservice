from app import app
from app.forms import LoginForm
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Pandoc Webservice')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)