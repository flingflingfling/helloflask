from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return 'welcome to my chatbox!'

@app.route('/user/<name>')
def user_page(name):
    return f'This is User {escape(name)}  page'

@app.route('/test')
def test_url():
    print(url_for('test_url'))
    print(url_for('hello'))
    print(url_for('user_page', name='jon don'))
    return 'test_page'