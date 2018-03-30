from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Adam'}

    posts = [
        {
            'author':{'username':'John'},
            'body': 'Beautiful day in Shiplake!'
        },

        {
            'author': {'username': 'Mark'},
            'body': 'Who wants some tea?'
        }

    ]

    return render_template('index.html', title='Home', posts = posts, user=user)