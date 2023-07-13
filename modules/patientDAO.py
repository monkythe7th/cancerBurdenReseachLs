# from mysql import connector
from flask import request
from ..modules import sqlQueries
# from ..modules.db_conn import Connection

class PatientDAO:

    

    def patient_demographic(db):

        #congfigure db
        
        today = request.form['date']
        firstname = request.form['firstname']
        surname = request.form['surname']
        gender = request.form['gender']
        facility_id = request.form['facility__identification__number']
        national_id = request.form['national__identification__number']
        dob = request.form['dob']
        age = request.form['age']
        physical_address = request.form['physical__address']
        phone = request.form['phone']
        level_of_education = request.form['level__of__education']
        occupation = request.form['occupation']
        marital_status = request.form['marital__status']
        religion = request.form['religion']
        no_of_children = request.form['number__of__children']
        next_of_kin = request.form['nok']
        Next_of_kin_phone = request.form['nok__phone']

        data = (today,firstname,surname,gender,facility_id,national_id,dob,age,physical_address,phone,level_of_education,occupation,marital_status,religion,next_of_kin,Next_of_kin_phone)    
        cur = conn.cursor()

        error = None

        try:
            cur.excercute(sqlQueries.Patient_Info_Sql(),data)
            conn.commit()
        except:
            conn.rollback()
            error = "not in database"
        
        return error

    def screening(db):
        # previous screening
        previous_screening = request.form['']
        previous_screening_type = request.form['']
        treatment = request.form['']
        date_of_results = request.form['']
        # current screening
        refering_facility = request.form['']
        family_planning = request.form['']
        hiv_status = request.form['']
        hts = request.form['']
        hiv_test_results = request.form['']
        purpose_of_visit = request.form['']
        screening_type = request.form['']
        screening_method = request.form['']
        screening_results = request.form['']
        management_and_treatment = request.form['']
        next_visit = request.form['']
        try:
            pass
        except:
            pass

    def tumour(db):
        incidence_date = request.form['']
        basis_of_diagnosis = request.form['']
        topography = request.form['']
        morphology = request.form['']
        laterlity = request.form['']
        stage = request.form['']

        pass

    def treatment(db):
        treatment_type = request.form['']
        treatment_date = request.form['']
        pass

    def source(db):
        institution = request.form['']
        ward = request.form['']
        case_no = request.form['']
        date_of_source = request.form['']
        laboratory = request.form['']
        lab_no = request.form['']
        pass

    def follow_up(db):
        date_of_last_contact = request.form['']
        state_of_last_contact = request.form['']
        cause_of_death = request.form['']
        refered_from = request.form['']
        ref_no1 = request.form['']
        refered_to = request.form['']
        ref_no2 = request.form['']
        pass

    def get_records():
        pass

    def get_one_record():
        
        pass