
import os

files = [
    r"d:\Final year\AskADoctor-main\templates\MyApp\about.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\adminlogin.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\adminsignup.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\admin_add_appointment.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\admin_add_doctor.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\admin_admit_patient.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\admin_base.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\admin_dashboard.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\admin_patient.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\CentersofExcellence.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\Covid19.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\Covid19Symptoms.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\Covid19Treatment.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\Covid19VaccineMyths.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\CovidResources.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\CovidTesting.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\CovidVaccination.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\doctorlogin.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\doctorsignup.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\doctor_appointment.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\doctor_base.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\doctor_dashboard.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\doctor_patient.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\home_book_appointment.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\patientlogin.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\patientsignup.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\patient_base.html",
    r"d:\Final year\AskADoctor-main\templates\MyApp\patient_dashboard.html",
]

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('{% load staticfiles %}', '{% load static %}')
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"No changes needed for {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
