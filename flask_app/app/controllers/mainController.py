from flask import render_template, request, url_for, redirect
from app.models.Meeting import Meeting
from app.models.Doctor import Doctor
from app.models.Patient import Patient
from app.models.Medical_interview import Medical_interview
from app.database.database import db
from sqlalchemy import asc, desc, func, extract, cast, text
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy
import time

engine = create_engine("postgresql://flaskapp:flaskapp@db:5432/flaskapp")


def index():
    return render_template("index.html")


def query1():
    with Session(engine) as session:
        st = time.time()

        q1 = (
            session.query(
                Patient.id.label("patid"),
                extract("year", func.age(Patient.born)).label("age"),
            )
            # .group_by(Patient.id)
            # .having(sqlalchemy.text("agee > 30"))
        )
        subq = q1.subquery()
        q1 = session.query(subq).where(text("age>=60"))
        # .statement.columns.keys()
        rows = q1.all()

        q2 = (
            session.query(
                Patient.id.label("patid"), func.count(Meeting.id).label("meets")
            )
            .join(Patient, Patient.id == Meeting.id_patient)
            .group_by(Patient.id)
            .having(func.count(Meeting.id) > 3)
        )
        rows = q2.all()

        q1_sub = q1.subquery()
        q2_sub = q2.subquery()

        q3 = (
            db.session.query(q1_sub.c.patid)
            .join(q2_sub, q2_sub.c.patid == q1_sub.c.patid)
            .group_by(q1_sub.c.patid)
            .order_by(q1_sub.c.patid)
        )
        rows = q3.all()

        # rows.filter(sqlalchemy.cast("age", sqlalchemy.DECIMAL) > 30)
        # rows = rows.all().keys()

        #  .group_by(Patient.id)
        #     .having(cast(func.age(Patient.born), sqlalchemy.DECIMAL) > 60)

        et = time.time()

        return render_template("query1.html", rows=rows)


def query2():
    with Session(engine) as session:
        st = time.time()
        rows = (
            session.query(
                Meeting.id_doctor, func.count(Meeting.id_doctor).label("bestdoctor")
            )
            .group_by(Meeting.id_doctor)
            .order_by(desc("bestdoctor"))
        )
        # print("HEEEEEEEEEEEEEsEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE1")
        # print(rows)
        rows = rows.first()
        best_doctor_id = rows.id_doctor
        rows = session.query(Doctor.medical_specialization).where(
            Doctor.id == best_doctor_id
        )
        # print("HEEEEEEEEEEEEEsEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE2222222222222222")
        # print(rows)
        rows = rows.first()
        best_doctor_med_spec = rows.medical_specialization
        best_doctor_med_spec = str(best_doctor_med_spec)
        rows = (
            session.query(Patient.surname, func.count(Meeting.id))
            .join(Meeting, Patient.id == Meeting.id_patient)
            .join(Doctor, Doctor.id == Meeting.id_doctor)
            .group_by(Patient.surname)
            .where(Doctor.medical_specialization == best_doctor_med_spec)
            .where(Patient.surname == "Hamill")
        )
        # print("HEEEEEEEEEEEEEsEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE3333333333333333333333333E")
        # print(rows)
        rows = rows.all()
        et = time.time()
        elapsed_time_orm_query = et - st

        st = time.time()
        raw_query_rows = session.execute(
            'Select "Patient".surname, COUNT("Meeting") FROM "Patient" \
        JOIN "Meeting" ON "Patient".id = "Meeting".id_patient\
        JOIN "Doctor" ON "Doctor".id = "Meeting".id_doctor\
        WHERE "Doctor".medical_specialization = (\
	    Select "Doctor".medical_specialization FROM "Doctor" WHERE "Doctor".id = (\
		Select "Meeting".id_doctor AS bestdoctor \
		from "Meeting"\
		GROUP BY "Meeting".id_doctor ORDER BY COUNT("Meeting") DESC LIMIT 1\
	))\
        AND "Patient".surname = \'Hamill\'\
        GROUP BY "Patient".surname\
        '
        )
        et = time.time()
        elapsed_time_raw_query = et - st

    return render_template(
        "query2.html",
        rows=rows,
        raw_query_rows=raw_query_rows,
        elapsed_time_orm_query=elapsed_time_orm_query,
        elapsed_time_raw_query=elapsed_time_raw_query,
    )
