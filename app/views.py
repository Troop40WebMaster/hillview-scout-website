__author__ = 'Robert'
from app import app
from flask import __version__
import platform

@app.route('/')
@app.route('/index')
def index():
    announce = []
    announce.append("New Hillview Scouting Website coming soon(ish)")
    announce.append("Powered by Python {} and Flask {}!".format(platform.python_version(), __version__))
    return '<br>'.join(announce)
