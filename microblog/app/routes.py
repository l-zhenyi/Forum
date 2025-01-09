from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse 
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username':'Daniel'}

    posts = [
        {
            'author': {'username': 'Shin'},
            'body': 'It is a lovely day to travel to Singapore'
        },
        {
            'author': {'username':'Ji Lin'},
            'body': 'There was a tiger sighting in the forest once.'
        }
    ]
    return render_template('index.html', title="Home Page", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('index')) 
    form = LoginForm() 
    if form.validate_on_submit(): 
        user = User.query.filter_by(username=form.username.data).first() 
        if user is None or not user.check_password(form.password.data): 
            flash('Invalid username or password') 
            return redirect(url_for('login')) 
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next') 
        if not next_page or url_parse(next_page).netloc != '': 
            next_page = url_for('index') 
            return redirect(next_page) 
        return redirect(url_for('index')) 
    return render_template('login.html', title='Sign In', form=form) 

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Clearing database for next session
# (venv) $ flask db downgrade base
# (venv) $ flask db upgrade

# Cleaning flask shell
#  >>> users = User.query.all() 
# >>> for u in users: 
# ...     db.session.delete(u) 
# ... 
# >>> posts = Post.query.all() 
# >>> for p in posts: 
# ...     db.session.delete(p) 
# ... 
# >>> db.session.commit() 