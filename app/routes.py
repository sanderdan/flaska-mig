from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sander'}
    posts = [
        {
            'author' : {'username':'Johnny'},
            'body': 'Nemos pizzeria, such pizza'
        },
        {
            'author': {'username': 'Sandahcity'},
            'body': 'Wow, Sannegårdens'
        }
    ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)