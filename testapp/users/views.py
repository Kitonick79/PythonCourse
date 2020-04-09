from flask import make_response
from flask import redirect
from flask import request
from flask import abort
from flask import session
from flask import url_for
from flask import render_template
from .models import User
from flask import Blueprint

app = Blueprint('users', __name__, template_folder='templates')


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
    return redirect(url_for('common.index'))


@app.route('/login')
def login_page():
    rendered_template = render_template(
        'login.tpl', 
        login_url=url_for('.login'),
        logout_url=url_for('.logout_page'),
    )
    return make_response(rendered_template)


@app.route('/logout', methods=['POST', 'GET'])
def logout_page():
    if request.method == 'GET':
        rendered_template = render_template('logout.tpl')
        return make_response(rendered_template)
    # method == POST
    session['username'] = 'anonymous'
    return redirect(url_for('common.index'))

