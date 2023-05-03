from flask import Flask, Blueprint, render_template, request, redirect, url_for, g
from .patientDAO import *
from .auth import *

bp = Blueprint('ui',__name__,url_prefix='/form')

@bp.route('/', methods=['POST','GET'])
# @login_required
def patient_demographic():
    if request.method == 'POST':
        try:
            PatientDAO.patient_demographic(request.form)
        finally:
            return redirect(url_for('ui.screening'))
    return render_template('demographic.html')

@bp.route('/screening')
# @login_required
def screening():
    if request.method == 'POST':
        try:
            PatientDAO.screening(request.form)
        finally:
            return redirect(url_for('ui.tumour'))
    return render_template('screening.html')
        
@bp.route('/tumour')
# @login_required
def tumour():
    return render_template('tumour_form.html')

@bp.route('/treatment')
# @login_required
def treatment():
    return render_template('treatment.html')

@bp.route('/source')
# @login_required
def source():
    return render_template('source_info.html')

@bp.route('/follow_up')
# @login_required
def follow_up():
    return render_template('followup.html')

@bp.route('/view_records')
# @login_required
def view_records():
    return render_template('index.html')
