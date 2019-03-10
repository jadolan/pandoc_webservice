import os

class Config(object):
    SECRET_KEY = 'dev'
    UPLOAD_FOLDER = '/uploads'
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'md', 'pdf', 'png', 'tex' ])