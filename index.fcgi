#!flask/bin/python
from flask import Flask, __version__
from flipflop import WSGIServer
import platform

app = Flask(__name__)

@app.route('/')
def hello():
    announce = []
    announce.append("New Hillview Scouting Website coming soon(ish)")
    announce.append("Powered by Python {} and Flask {}!".format(platform.python_version(), __version__))
    return '<br>'.join(announce)

WSGIServer(app).run()