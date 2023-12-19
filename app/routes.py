from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/layout_static')
def layout_static():
    return render_template('layout_static')

@app.route('/layout_sidenav_light')
def layout_sidenav_light():
    return render_template('layout_sidenav_light')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/password')
def password():
    return render_template('password.html')
@app.route('/page_401')
def page_401():
    return render_template('page_401.html')
@app.route('/page_404')
def page_404():
    return render_template('page_404.html')
@app.route('/page_500')
def page_500():
    return render_template('page_500.html')
@app.route('/charts')
def charts():
    return render_template('charts.html')
@app.route('/tables')
def tables():
    return render_template('tables.html')