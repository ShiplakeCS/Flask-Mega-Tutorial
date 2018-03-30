import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MCLy0V22y2pINmsZxcjY1mZ683gSZWVS'