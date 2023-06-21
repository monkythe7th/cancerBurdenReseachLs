import functools
from flask import Flask, render_template, redirect, request, Blueprint, url_for, flash, g, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..api import create, read as getter

bp = Blueprint("auth",__name__,url_prefix='/auth')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user == None:
            return redirect('login')
        return view(**kwargs)
    return wrapped_view

def admin_only(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user_type != 'admin' or g.user_type == None:
            return redirect(url_for('index'))
        return view(**kwargs)
    return wrapped_view

@bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = getter.read({'username':username})
        if not user:
            error = "invalid username or password"
            flash(error)
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
    return render_template('login.html')

@bp.route('/create_user', methods=['POST','GET'])
# @login_required
# @admin_only
def create_user():
    if request.method == 'POST':
        # fullName = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['auth--role']
        user = {
            # 'name': fullName,
            'username': username,
            'email': email,
            'user_type': role,
            'password': password
        }
        error = None
        try:
            u = getter.read({'username':username})
            if not u or not error: return
            create.create(user)
        except Exception:
            flash(error,'error')
        finally:
            pass
    return render_template('auth.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_user():
    uid = session.get('user_id')
    if not uid:
        g.user = None
    else:
        g.user = {}
