import os

class Config(object):
    """
    # TODO: When deployed on server, hardcoded SECRET_KEY value becomes unique and difficult
    Should only be known to trusted maintainers of the site
    #
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-in-a-million-years'
    # Proects against CSRF. Generates secure tokens and signatures.