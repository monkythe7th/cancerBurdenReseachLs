
class PatientDAO:


    def patient_demographic(form_data):
        today = form_data['date']
        fistname = form_data['firstname']
        surname = form_data['surname']
        gender = form_data['gender']
        facility_id = form_data['facility__identification__number']
        national_id = form_data['national__identification__number']
        dob = form_data['dob']
        age = form_data['age']
        physical_address = form_data['physical__address']
        phone = form_data['phone']
        level_of_education = form_data['level__of__education']
        occupation = form_data['occupation']
        marital_status = form_data['marital__status']
        religion = form_data['religion']
        no_of_children = form_data['number__of__children']
        next_of_kin = form_data['nok']
        Next_of_kin_phone = form_data['nok__phone']
        try:
            pass
        except:
            return

    def screening(form_data):
        # previous screening
        previous_screening = form_data['']
        previous_screening_type = form_data['']
        treatment = form_data['']
        date_of_results = form_data['']
        # current screening
        refering_facility = form_data['']
        family_planning = form_data['']
        hiv_status = form_data['']
        hts = form_data['']
        hiv_test_results = form_data['']
        purpose_of_visit = form_data['']
        screening_type = form_data['']
        screening_method = form_data['']
        screening_results = form_data['']
        management_and_treatment = form_data['']
        next_visit = form_data['']
        try:
            pass
        except:
            pass

    def tumour(form_data):
        incidence_date = form_data['']
        basis_of_diagnosis = form_data['']
        topography = form_data['']
        morphology = form_data['']
        laterlity = form_data['']
        stage = form_data['']

        pass

    def treatment(form_data):
        treatment_type = form_data['']
        treatment_date = form_data['']
        pass

    def source(form_data):
        institution = form_data['']
        ward = form_data['']
        case_no = form_data['']
        date_of_source = form_data['']
        laboratory = form_data['']
        lab_no = form_data['']
        pass

    def follow_up(form_data):
        date_of_last_contact = form_data['']
        state_of_last_contact = form_data['']
        cause_of_death = form_data['']
        refered_from = form_data['']
        ref_no1 = form_data['']
        refered_to = form_data['']
        ref_no2 = form_data['']
        pass

