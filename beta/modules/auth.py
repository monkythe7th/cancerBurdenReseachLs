import functools
from flask import Flask, render_template, redirect, request, Blueprint, url_for, flash, g, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..api import create, read as getter

bp = Blueprint("auth",__name__,url_prefix='/auth')

# 
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user == None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

# Administrator permissions 
def admin_only(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['user_type'] != 'admin' or g.user['user_type'] == None: return redirect(url_for('index'))
        return view(**kwargs)
    return wrapped_view

# read / write permissions for Administrator and Registrar
def read_write_perm(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['user_type'] == 'admin' or g.user['user_type'] == 'registrar' or g.user['user_type'] != None: return view(**kwargs)
        return redirect(url_for('index'))
    return wrapped_view

# login
@bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = getter.read('admin',{'username':username})
        if not user:
            error = "invalid username"
            flash(error)
        elif not check_password_hash(user['password'],password): 
            error = "invalid password"
            flash(error)
        if error is None:
            session.clear()
            session['user_id'] = user['username']
            return redirect(url_for('index'))
    return render_template('login.html')

# creating a new user
@bp.route('/create_user', methods=['POST','GET'])
@login_required
# @admin_only
def create_user():
    if request.method == 'POST':
        fullName = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['auth--role']
        user = {
            'name': fullName,
            'username': username,
            'email': email,
            'user_type': role,
            'password': generate_password_hash(password)
        }
        error = None
        try:
            u = getter.read('admin',{'username':username})
            if u: flash('')
            create.create('admin',user)
        except Exception:
            flash(error,'error')
        finally:
            return redirect(url_for('ui.admin_dash'))
    return render_template('auth.html')

#  update user info
@bp.route('/update')
@admin_only
def update_user():
    return render_template('authupdate.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# load a user into the session
@bp.before_app_request
def load_logged_user():
    uid = session.get('user_id')
    if not uid:
        g.user = None
    else:
        g.user = getter.read('admin',{'username':uid})

