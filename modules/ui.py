import traceback
from flask import Flask, Blueprint, render_template, request, redirect, url_for, g, flash, session
from .patientDAO import *
from .auth import *
from ..api import read as getter

bp = Blueprint('ui',__name__,url_prefix='/ui')
Patient = PatientDAO()

# patient information form
@bp.route('/', methods=['POST','GET'], endpoint='demographic')
@login_required
@read_write_perm
def demographic():
    error = None
    if request.method == 'POST':
        try:
            patient = Patient.demographic()
            session['current_patient']=patient
        finally:
            if error is None: return redirect(url_for('ui.screening'))
            flash(error,'warning')
    return render_template('demographic.html')

# cancer screening form
@bp.route('/screening/', methods=['POST','GET'])
@login_required
@read_write_perm
def screening():
    try:
        Patient.set_patient(session['patient'])
        if request.method == 'POST':
            try:
                patient_id = Patient.screening()
            except:
                Patient.set_patient(session['patient'])
                patient_id = Patient.screening()
            finally:
                return redirect(url_for('ui.review',patient_id=patient_id))
    except KeyError:
        error = "patient not defined"
        flash(error)
    return render_template('screening.html')

# cancer tumour marker form
@bp.route('/tumour/<nat_id>', methods=['POST','GET'])
@login_required
@read_write_perm
def tumour(nat_id):
    g.patient = Patient.get_one_record(nat_id) if nat_id else redirect(url_for('ui.demographic'))
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
@bp.route('/update/<form>/')
@login_required
@read_write_perm
def update_record(form):
    if session['patient']:
        patient = session['patient']
        if form == 'tumour':
            return redirect(url_for('ui.tumour', nat_id=patient['national_id']))
        elif form == 'screening':
            return redirect(url_for('ui.screening'))
        elif form == 'treatment':
            return redirect(url_for())
        elif form == 'demographic':
            return redirect(url_for())

# update patient info
@bp.route('/update/', methods=['POST','GET'])
@login_required
@read_write_perm
def update_base():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        patient_form = request.form['patient_form']
        patient = Patient.get_one_record(patient_id)
        if patient:
            session['patient'] = patient
            return redirect(url_for('ui.update_record', form=patient_form))
    try:
        if session['current_patient']:
            pass
    except KeyError:
        pass
    return render_template('update.html')

# review single patient
@bp.route('/review/<patient_id>')
@login_required
def review(patient_id):
    patient = ''
    message = None
    try:
        if patient_id:
            patient = Patient.get_one_record(patient_id)
        else:
            patient = Patient.get_one_record()
    except:
        patient = None
        message = traceback.print_last()
    finally:
        g.patient = patient
        flash(message)
        return render_template('get_one.html')

# posting form to database
@bp.route('/post/<save>/<nat_id>', methods=['POST','GET'])
@login_required
def post_record(save, nat_id):
    if nat_id: Patient.post_record(nat_id)
    if save == 'home':
        return redirect(url_for('index'))
    if save == 'continue':
        if 'tumour_markers' not in Patient.patient.keys():
            return redirect(url_for('ui.tumour',nat_id=nat_id))
        else:
            return redirect(url_for('ui.view_records'))

# authentication ui dashboard
@bp.route('auth/dashboard')
@login_required
# @read_write_perm
def admin_dash():
    g.users = getter.get_all('admin')
    # session['users'] = g.users
    return render_template('authdash.html')