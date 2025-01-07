import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #TODO: When deployed on server, hardcoded SECRET_KEY value becomes unique and difficult
    #Should only be known to trusted maintainers of the site
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-in-a-million-years'
    # Proects against CSRF. Generates secure tokens and signatures.

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False 