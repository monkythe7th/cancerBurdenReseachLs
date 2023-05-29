# Query that ineserts Patient Information into the database

def Patient_Info_Sql():
    sql = """INSERT INTO patient_information(Today_date,
                                            FirstName,
                                            LastName,
                                            Gender,
                                            FacilityIdNo,
                                            NationalIdNo,
                                            DOB,
                                            Age,
                                            Address,
                                            PhoneNo,
                                            Education,
                                            Occupation,
                                            MaritalStatus,
                                            Religion,
                                            NumberOfChildren,
                                            NOK,
                                            NOKNo)
                                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    return(sql)

# Query that inserts Patients Screening Progress and process records into the database

def Screening_Info_Sql():
    sql = """INSERT INTO screening(Patient_id,
                                    Previous_id,
                                    Date_results,
                                    Reffering_facility,
                                    Family_planing_methods
                                    HIV_status,
                                    HTS_offered
                                    Purpose_of_visit,
                                    Type_of_screening,
                                    methods_of_screening
                                    screening_results,
                                    Management_and_treatment,
                                    Next_visit)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s))"""
    return(sql)

def treatment_Info_Sql():
    sql = """INSERT INTO treatment(Patient_id,
                                    treatment_type,
                                    treatment_date,
                                    VALUES(%s,%s,%s))"""
    return(sql)

def tumor_Info_Sql():
    sql = """INSERT INTO tumor_form(Patient_id,
                                    incident_date,
                                    basis_of_diagnosis,
                                    topography,
                                    morphology,
                                    laterlity,
                                    stage)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s))"""
    return(sql)

def source_Info_Sql():
    sql = """INSERT INTO tumor_form(Patient_id,
                                    institution,
                                    ward,
                                    case_no,
                                    data_of_source,
                                    laborytory)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s))"""
    return(sql)


