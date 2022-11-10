from flask import render_template, request, url_for, redirect
from app.models.Meeting import Meeting
from app.models.Doctor import Doctor
from app.models.Patient import Patient
from app.database.database import db
from sqlalchemy import asc

ROWS_PER_PAGE = 2


def meetings():
    if request.method == "POST":
        # pesel = request.form["pesel"]
        # name = request.form["name"]
        # surname = request.form["surname"]
        # email = request.form["email"]
        # phone_num = request.form["phone_num"]
        # born = request.form["born"]
        # address = request.form["address"]
        # disablity = request.form["disability"]
        # medical_specialization = request.form["medical_specialization"]
        # meeting = Doctor(
        #     pesel=str(pesel),
        #     email=email,
        #     name=name,
        #     surname=surname,
        #     phone_num=phone_num,
        #     born=born,
        #     address=address,
        #     disablity=bool(disablity),
        #     medical_specialization=medical_specialization,
        # )
        # db.session.add(meeting)
        # db.session.commit()

        return redirect(url_for("blueprint.meetings"))
    else:
        # meetings = Doctor.query.order_by(asc("id"))
        page = request.args.get("page", 1, type=int)
        meetings = Meeting.query.paginate(page=page, per_page=ROWS_PER_PAGE)
        needed_doctors = {}
        needed_patients = {}
        for meeting in meetings.items:
            needed_doctors[meeting.id_doctor] = Doctor.query.get_or_404(
                meeting.id_doctor
            )
            needed_patients[meeting.id_patient] = Patient.query.get_or_404(
                meeting.id_doctor
            )

        # print("HEEEEEEEEEEEEEEEEREEEEEEEEEEEEEEEEEEEEEEE", meetings.items[1].id_doctor)
        print("HEEEEEEEEEEEEEEEEREEEEEEEEEEEEEEEEEEEEEEE", needed_doctors)

        return render_template(
            "meetings.html",
            doctors=needed_doctors,
            meetings=meetings,
            patients=needed_patients,
        )


def meeting(id):
    meeting = Meeting.query.get_or_404(id)
    return render_template("meeting.html", meeting=meeting)


# def meeting_add():
#     return render_template("add_meeting.html")


# def meeting_edit(id):
#     meeting = Doctor.query.get_or_404(id)
#     if request.method == "POST":

#         try:
#             pesel = str(request.form["pesel"])
#         except:
#             pesel = meeting.pesel

#         try:
#             disablity = bool(request.form["disability"])
#         except:
#             disablity = meeting.disablity

#         name = request.form["name"] if request.form["name"] != "" else meeting.name
#         surname = (
#             request.form["surname"] if request.form["surname"] != "" else meeting.surname
#         )
#         email = request.form["email"] if request.form["email"] != "" else meeting.email
#         phone_num = (
#             request.form["phone_num"]
#             if request.form["phone_num"] != ""
#             else meeting.phone_num
#         )
#         born = request.form["born"] if request.form["born"] != "" else meeting.born
#         address = (
#             request.form["address"] if request.form["address"] != "" else meeting.address
#         )
#         medical_specialization = (
#             request.form["medical_specialization"]
#             if request.form["medical_specialization"] != ""
#             else meeting.medical_specialization
#         )

#         meeting.pesel = pesel
#         meeting.email = email
#         meeting.name = name
#         meeting.surname = surname
#         meeting.phone_num = phone_num
#         meeting.born = born
#         meeting.address = address
#         meeting.disability = disablity
#         meeting.medical_specialization = medical_specialization

#         db.session.add(meeting)
#         db.session.commit()

#         return redirect(url_for("blueprint.meetings"))
#     else:
#         return render_template("edit_meeting.html", meeting=meeting)


# def meeting_delete(id):
#     meeting = Doctor.query.get_or_404(id)
#     db.session.delete(meeting)
#     db.session.commit()
#     return redirect(url_for("blueprint.meetings"))
