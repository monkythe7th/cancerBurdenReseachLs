from flask import Flask, Blueprint, render_template, request, redirect, url_for, g
from .patientDAO import *
from .auth import *

bp = Blueprint('ui',__name__,url_prefix='/ui')

@bp.route('/', methods=['POST','GET'])
# @login_required
def patient_demographic():
    if request.method == 'POST':
        try:
            PatientDAO.patient_demographic(request.form)
        finally:
            return redirect(url_for('ui.screening'))
    return render_template('demographic.html')

@bp.route('/screening', methods=['POST','GET'])
# @login_required
def screening():
    if request.method == 'POST':
        try:
            PatientDAO.screening(request.form)
        finally:
            return redirect(url_for('ui.review',name='screening'))
    return render_template('screening.html')
        
@bp.route('/tumour', methods=['POST','GET'])
# @login_required
def tumour():
    if request.method == 'POST':
        try :
            PatientDAO.tumour(request.form)
        finally:
            return redirect(url_for('ui.treatment'))
    return render_template('tumour_form.html')

@bp.route('/treatment', methods=['POST','GET'])
# @login_required
def treatment():
    if request.method == 'POST':
        try :
            PatientDAO.treatment(request.form)
        finally:
            return redirect(url_for('ui.source'))
    return render_template('treatment.html')

@bp.route('/source', methods=['POST','GET'])
# @login_required
def source():
    if request.method == 'POST':
        try :
            PatientDAO.source(request.form)
        finally:
            return redirect(url_for('ui.follow_up'))
    return render_template('source_info.html')

@bp.route('/follow_up', methods=['POST','GET'])
# @login_required
def follow_up():
    if request.method == 'POST':
        try :
            PatientDAO.follow_up(request.form)
        finally:
            return redirect(url_for('ui.review',name='all'))
    return render_template('followup.html')

@bp.route('/view_records')
# @login_required
def view_records():
    records = PatientDAO.get_records()
    return render_template('get_all.html',records=records)

@bp.route('/update/<form>')
# @login_required
def update_record(form):
    pass

@bp.route('/review/<name>')
# @login_required
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
        return patient
    return render_template('get_one.html')
