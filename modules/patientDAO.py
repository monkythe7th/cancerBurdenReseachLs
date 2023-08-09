# from mysql import connector
from flask import request
from ..api import create, read as getter, update, delete
# from ..modules import sqlQueries
# from ..modules.db_conn import Connection

class PatientDAO:

    def __init__(self) -> None:
        self.patient = {}

    def demographic(self):
        
        today = request.form['date']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
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
        next_of_kin_phone = request.form['nok__phone']

        data = {
            'input_date':today,
            'firstname':firstname,
            'lastname':lastname,
            'gender':gender,
            'facility_id':facility_id,
            'dob':dob,
            'age':age,
            'physical_address':physical_address,
            'phone':phone,
            'level_of_education':level_of_education,
            'occupation':occupation,
            'marital_status':marital_status,
            'religion':religion,
            'no_of_children':no_of_children,
            'next_of_kin':next_of_kin,
            'next_of_kin_phone':next_of_kin_phone
        }

        error = None

        try:
            self.patient['national_id'] = national_id
            self.patient['demographic'] = data
        except:
            error = "not in database"
        
        return self.patient

    def screening(self):
        # previous screening
        
        # current screening
        family_planning = request.form['family__planning']
        hts = request.form['hts__offered']
        hiv_test_results = request.form['hiv__results']
        purpose_of_visit = request.form['purpose__visit']
        screening_type = request.form['screening__type']
        screening_method = request.form['screening__methods']
        screening_results = request.form['screening__results']
        referal = request.form['referal']
        next_visit = request.form['next__visit']
        
        data = {
            'family_planning':family_planning,
            'hts':hts,
            'hiv_test_results':hiv_test_results,
            'purpose_of_visit':purpose_of_visit,
            'screening_type':screening_type,
            'screening_method':screening_method,
            'screening_results':screening_results,
            'referal':referal,
            'next_visit':next_visit
        }

        try:
            self.patient['screening'] = data
        except:
            pass
        finally:
            return self.patient['national_id']

    def tumour(self):
        incidence_date = request.form['']
        basis_of_diagnosis = request.form['']
        topography = request.form['']
        morphology = request.form['']
        laterlity = request.form['']
        stage = request.form['']

        pass

    def treatment(self):
        treatment_type = request.form['']
        treatment_date = request.form['']
        pass

    def source(self):
        institution = request.form['']
        ward = request.form['']
        case_no = request.form['']
        date_of_source = request.form['']
        laboratory = request.form['']
        lab_no = request.form['']
        pass

    def follow_up(self):
        date_of_last_contact = request.form['']
        state_of_last_contact = request.form['']
        cause_of_death = request.form['']
        refered_from = request.form['']
        ref_no1 = request.form['']
        refered_to = request.form['']
        ref_no2 = request.form['']
        pass

    def get_records(self):
        return getter.get_all('patient')

    def get_one_record(self,nat_id=None):
        if self.patient: return self.patient
        return getter.read('patient',{'national_id':nat_id})

    def set_patient(self, patient: dict) -> None:
        self.patient = patient

    def post_record(self, nat_id):
        if nat_id and self.patient: 
            if self.patient['national_id'] == nat_id:
                patient = getter.read('patient',{'national_id':nat_id})
            if patient: return 'patient already exists'
            create.create('patient', self.patient)
        