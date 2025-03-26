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

    MAIL_SERVER = os.environ.get('MAIL_SERVER') 
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25) 
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
    ADMINS = ['your-email@example.com'] #TODO: SET WEBSITE ADMIN EMAILS
    POSTS_PER_PAGE = 25 # TODO: SET NUMBER OF POSTS PER PAGE
