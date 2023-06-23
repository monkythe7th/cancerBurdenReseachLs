from flask import Flask, Blueprint, render_template, request, redirect, url_for, g, flash, session
from .patientDAO import *
from .auth import *
from ..api import read as getter

bp = Blueprint('ui',__name__,url_prefix='/ui')

# patient information form
@bp.route('/', methods=['POST','GET'])
@login_required
@read_write_perm
def patient_demographic():
    error = None
    if request.method == 'POST':
        try:
            error = PatientDAO.patient_demographic(request.form)
        finally:
            if error == None: return redirect(url_for('ui.screening'))
            flash(error,'warning')
    return render_template('demographic.html')

# cancer screening form
@bp.route('/screening', methods=['POST','GET'])
@login_required
@read_write_perm
def screening():
    if request.method == 'POST':
        try:
            PatientDAO.screening(request.form)
        finally:
            return redirect(url_for('ui.review',name='screening'))
    return render_template('screening.html')

# cancer tumour marker form
@bp.route('/tumour', methods=['POST','GET'])
@login_required
@read_write_perm
def tumour():
    if request.method == 'POST':
        try :
            PatientDAO.tumour(request.form)
        finally:
            return redirect(url_for('ui.treatment'))
    return render_template('tumour_form.html')

# recommended treatment form
@bp.route('/treatment', methods=['POST','GET'])
@login_required
@read_write_perm
def treatment():
    if request.method == 'POST':
        try :
            PatientDAO.treatment(request.form)
        finally:
            return redirect(url_for('ui.source'))
    return render_template('treatment.html')

# source of information form
@bp.route('/source', methods=['POST','GET'])
@login_required
@read_write_perm
def source():
    if request.method == 'POST':
        try :
            PatientDAO.source(request.form)
        finally:
            return redirect(url_for('ui.follow_up'))
    return render_template('source_info.html')

# follow up form
@bp.route('/follow_up', methods=['POST','GET'])
@login_required
@read_write_perm
def follow_up():
    if request.method == 'POST':
        try :
            PatientDAO.follow_up(request.form)
        finally:
            return redirect(url_for('ui.review',name='all'))
    return render_template('followup.html')

# view records, any one who has log in credentials can use this
@bp.route('/view_records')
@login_required
def view_records():
    records = PatientDAO.get_records()
    return render_template('get_all.html',records=records)

# rupdate patient info
@bp.route('/update/<form>')
@login_required
@read_write_perm
def update_record(form):
    pass

# review single patient
@bp.route('/review/<name>')
@login_required
def review(name):
    patient = ''
    try:
        if name == 'screening':
            patient = PatientDAO.get_one_record()
        elif name == 'all':
            pass
    except:
        pass
    finally:
        g.patient = patient
    return render_template('get_one.html')

# authentication ui dashboard
@bp.route('auth/dashboard')
@login_required
@read_write_perm
def admin_dash():
    g.users = getter.get_all()
    # session['users'] = g.users
    return render_template('authdash.html')