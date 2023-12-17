from app import app
from flask import render_template

@app.route('/')
def home():
    return 'Hello world!'
@app.route('/curriculo')
def curriculo():
    return render_template('index.html')