from flask import Flask, Blueprint, render_template, request, redirect, url_for, g, flash, session
from .patientDAO import *
from .auth import *
from ..api import read as getter

bp = Blueprint('ui',__name__,url_prefix='/ui')
Patient = PatientDAO()

# patient information form
@bp.route('/', methods=['POST','GET'])
@login_required
@read_write_perm
def patient_demographic():
    error = None
    if request.method == 'POST':
        try:
            error = Patient.patient_demographic()
        finally:
            if error is None: return redirect(url_for('ui.screening'))
            flash(error,'warning')
    return render_template('demographic.html')

# cancer screening form
@bp.route('/screening', methods=['POST','GET'])
@login_required
@read_write_perm
def screening():
    if request.method == 'POST':
        patient_id = ''
        try:
            patient_id = Patient.screening()
        finally:
            return redirect(url_for('ui.review',patient_id=patient_id))
    return render_template('screening.html')

# cancer tumour marker form
@bp.route('/tumour', methods=['POST','GET'])
@login_required
@read_write_perm
def tumour():
    if request.method == 'POST':
        try :
            Patient.tumour()
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
            Patient.treatment()
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
            Patient.source()
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
            Patient.follow_up()
        finally:
            return redirect(url_for('ui.review'))
    return render_template('followup.html')

# view records, any one who has log in credentials can use this
@bp.route('/view_records')
@login_required
def view_records():
    g.records = Patient.get_records()
    return render_template('get_all.html')

# update patient info
@bp.route('/update/<form>')
@login_required
@read_write_perm
def update_record(form):
    pass

# update patient info
@bp.route('/update/')
@login_required
@read_write_perm
def update_base():
    pass

# review single patient
@bp.route('/review/<patient_id>')
@login_required
def review(patient_id = g.patient):
    patient = ''
    try:
        if patient_id:
            patient = Patient.get_one_record(patient_id)
        else:
            patient = Patient.get_one_record()
    except:
        patient = 'No Record found'
    finally:
        g.patient = patient
    return render_template('get_one.html')

# posting form to database
@bp.route('/post/<save>', methods=['POST'])
@login_required
def post_record(save):
    Patient.post_record()
    if save == 'home':
        return redirect(url_for('index'))
    if Patient.patient['tumour_markers']:
        return redirect(url_for('ui.view_records'))
    else:
        return redirect(url_for('ui.tumour'))

# authentication ui dashboard
@bp.route('auth/dashboard')
@login_required
# @read_write_perm
def admin_dash():
    g.users = getter.get_all('admin')
    # session['users'] = g.users
    return render_template('authdash.html')