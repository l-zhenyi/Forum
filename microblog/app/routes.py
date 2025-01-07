from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title="Home Page", user = user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect ('index')
    return render_template('login.html', tile='Sign In', form=form)

