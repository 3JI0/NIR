from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lexa'}
    books = [
        {
            'author': {'username': 'Pushkin'},
            'named': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Esenin'},
            'named': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, books=books)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)