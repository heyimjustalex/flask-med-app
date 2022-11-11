from flask import render_template, request, url_for, redirect
from app.models.Meeting import Meeting
from app.models.Doctor import Doctor
from app.models.Patient import Patient
from app.models.Medical_interview import Medical_interview
from app.database.database import db
from sqlalchemy import asc,desc, func
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import time

engine = create_engine("postgresql://flaskapp:flaskapp@db:5432/flaskapp")

def index():
    return render_template("index.html")

def query1():
    pass

def query2():
    with Session(engine) as session:
        st = time.time()
        rows = session.query(Meeting.id_doctor,func.count(Meeting.id_doctor).label('bestdoctor')).group_by(Meeting.id_doctor).order_by(desc('bestdoctor'))
        print("HEEEEEEEEEEEEEsEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECYCEEEEE")
        print(rows)
        rows = rows.first()
        best_doctor_id = rows.id_doctor      
        rows = session.query(Doctor.medical_specialization).where(Doctor.id==best_doctor_id)
        print("HEEEEEEEEEEEEEsEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECYCEEEEE22222222222222222")
        print(rows)
        rows = rows.first()
        best_doctor_med_spec = rows.medical_specialization
        best_doctor_med_spec = str(best_doctor_med_spec)
        rows = session\
        .query(Patient.surname,func.count(Meeting.id))\
        .join(Meeting, Patient.id==Meeting.id_patient)\
        .join(Doctor,Doctor.id == Meeting.id_doctor)\
        .group_by(Patient.surname)\
        .where(Doctor.medical_specialization==best_doctor_med_spec)\
        .where(Patient.surname=='Hamill')
        print("HEEEEEEEEEEEEEsEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECYCEEEE3333333333333333333333333E")
        print(rows)
        rows = rows.all()
        et = time.time()
        elapsed_time_orm_query = et - st

        st = time.time()
        raw_query_rows = session.execute\
        ('Select "Patient".surname, COUNT("Meeting") FROM "Patient" \
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
        ')
        et = time.time()
        elapsed_time_raw_query = et - st
    
    return render_template("query2.html", rows=rows, raw_query_rows=raw_query_rows, elapsed_time_orm_query = elapsed_time_orm_query,elapsed_time_raw_query =elapsed_time_raw_query)