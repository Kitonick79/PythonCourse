from flask import make_response
from flask import Blueprint, session, render_template, url_for

app = Blueprint(__name__, __name__, template_folder='templates')


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
    else:
        username = 'anonymous'
    login_page_url = url_for('testapp.users.views.login_page')
    return make_response(render_template('index.tpl', username=username, login_page_url=login_page_url))
