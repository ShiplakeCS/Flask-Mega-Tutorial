import os

basedir = os.path.abspath(os.path.dirname(__file__))  # Get the folder for this file

class Config(object):
    # Get the secret key either from the CLI environment when the app is run, or use the included key as a fall-back.
    # It is safer to run the app with a newly generated key each time as then no-one will know what it is, even if they
    # access this source code and see the hard-coded key.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MCLy0V22y2pINmsZxcjY1mZ683gSZWVS'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False