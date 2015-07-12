__author__ = 'Robert'
from flask import render_template
from app import app

@app.route('/')
def landing():
    return render_template('landing.html', title='Home', subpage='home')

@app.route('/troop40')
def troop40():
    return render_template('troop40.html', title='Troop 40', subpage='troop')

@app.route('/pack40')
def pack40():
    return render_template('pack40.html', title='Pack 40', subpage='pack')

@app.route('/crew40')
def crew40():
    return render_template('crew40.html', title='Crew 40', subpage='crew')
