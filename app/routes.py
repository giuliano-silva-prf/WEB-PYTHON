from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return redirect(url_for('fcurriculo'))
@app.route('/curriculo')
def fcurriculo():
    return render_template('index.html')