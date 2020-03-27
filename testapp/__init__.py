from flask import Flask, make_response, render_template, session, abort
from flask import url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
    else: 
        username = 'anonymous' 
    login_page_url = url_for('login_page')
    return make_response(render_template('index.tpl', username=username, login_page_url=login_page_url))

@app.route('/login_processor', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user     = User.query.filter_by(username= username).first()
    if user and user.password == password:
        session['username'] = username
    else: 
        abort(403)
    return redirect(url_for('index'))

@app.route('/login')
def login_page():
    login_url = url_for('login')
    rendered_template = render_template('login.tpl', login_url = login_url)
    return make_response(rendered_template)


'''
Todo:
1. Develop logout for a session -- add link to logout
2. Handle LaTex.csv file
'''


