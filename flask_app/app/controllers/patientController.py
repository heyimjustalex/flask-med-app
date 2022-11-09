from flask import render_template, request, url_for, redirect
from app.models.Patient import Patient
from app.database.database import db
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import asc


def patients():
    patients = Patient.query.order_by(asc("id"))
    return render_template("index.html", patients=patients)


def patient(id):
    patient = Patient.query.get_or_404(id)
    return render_template("patient.html", patient=patient)


def patient_add():
    if request.method == "POST":
        pesel = request.form["pesel"]
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        phone_num = request.form["phone_num"]
        born = request.form["born"]
        print("BORNNNNNNNNNNNNNNN", born)
        address = request.form["address"]
        disablity = request.form["disability"]
        medical_offer = request.form["medical_offer"]
        patient = Patient(
            pesel=str(pesel),
            email=email,
            name=name,
            surname=surname,
            phone_num=phone_num,
            born=born,
            address=address,
            disablity=bool(disablity),
            medical_offer=medical_offer,
        )
        db.session.add(patient)
        db.session.commit()

        return redirect(url_for("blueprint.patients"))
    else:
        return render_template("add_patient.html")


# # update patient
# def patient_edit(id):
#     patient = patient.query.get_or_404(id)
#     if request.method == "POST":

#         name = request.form["name"] if request.form["name"] != "" else patient.name
#         surname = (
#             request.form["surname"]
#             if request.form["surname"] != ""
#             else patient.surname
#         )
#         email = request.form["email"] if request.form["email"] != "" else patient.email

#         try:
#             age = int(request.form["age"])
#         except:
#             age = patient.age

#         patient.email = email
#         patient.name = name
#         patient.surname = surname
#         patient.age = age

#         db.session.add(patient)
#         db.session.commit()

#         return redirect(url_for("blueprint.patients"))
#     else:
#         return render_template("edit_patient.html", patient=patient)


# # delete patient
# def patient_delete(id):
#     patient = patient.query.get_or_404(id)
#     db.session.delete(patient)
#     db.session.commit()
#     return redirect(url_for("blueprint.patients"))
