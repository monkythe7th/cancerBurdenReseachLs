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
    return render_template('demographics.html')

@bp.route('/screening')
# @login_required
def screening():
    if request.method == 'POST':
        try:
            PatientDAO.screening(request.form)
        finally:
            return redirect(url_for('ui.tumour'))
    return render_template('screening.html')
        
@bp.route('tumour')
# @login_required
def tumour():
    pass

# @login_required
def treatment():
    pass

# @login_required
def source():
    pass

# @login_required
def follow_up():
    pass
