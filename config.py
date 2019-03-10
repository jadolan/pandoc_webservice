from os.path import join, dirname, realpath

class Config(object):
    SECRET_KEY = 'dev'
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'app/static/uploads')
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'md', 'pdf', 'png', 'tex' ])