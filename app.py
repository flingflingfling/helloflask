from flask import Flask, render_template
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
@app.route('/main')
@app.route('/home')
def hello():
    return 'welcome to my chatbox!'

@app.route('/user/<name>')
def user_page(name):
    return f'This is User {escape(name)}  page'

@app.route('/index')
def index():
    return render_template('index.html', name=name, movies=movies)
     
@app.route('/test')
def test_url():
    print(url_for('test_url'))
    print(url_for('hello'))
    print(url_for('user_page', name='jon don'))
    return 'test_page'