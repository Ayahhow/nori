from flask import request, redirect, url_for, render_template
from noriart import app

@app.route('/')
def show_toppage():
    return render_template('top.html')

@app.route('/test2')
def show_test2():
    return render_template('test2.html')

@app.route('/iiwake')
def show_setsumei():
    return render_template('iiwake.html')
