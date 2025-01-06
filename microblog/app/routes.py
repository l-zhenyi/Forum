from flask import render_template
from app import app

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

