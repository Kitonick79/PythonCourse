from flask import make_response
from flask import redirect
from flask import request
from flask import abort
from flask import session
from flask import url_for
from flask import render_template
from .models import User
from flask import Blueprint

app = Blueprint(__name__, __name__, template_folder='templates')


def authCheck(f):
    def wrapper(*args, **kwargs):
        if session['username'] != 'anonymous': return f()
    return wrapper


@app.route('/login_processor', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username = username).first()
    if user and user.password == password:
        session['username'] = username
    else:
        abort(403)
    return redirect(url_for('testapp.common.views.index'))


@app.route('/login')
def login_page():
    rendered_template = render_template('login.tpl', login_url= url_for('testapp.users.views.login'))
    return make_response(rendered_template)


@app.route('/logout_processor', methods = ['POST'])
@authCheck
def logout():
    session['username'] = 'anonymous'
    return redirect(url_for('testapp.common.views.index'))


@app.route('/logout')
def logout_page():
    logout_url = url_for('testapp.users.views.logout')
    rendered_template = render_template('logout.tpl', logout_url = logout_url)
    return make_response(rendered_template)
