from flask import request, redirect, url_for, render_template
from noriart import app

@app.route('/')
def show_firstpage():
    return render_template('test.html')

@app.route('/test2')
def show_test2():
    return render_template('test2.html')
