from app.database.database import db
from sqlalchemy.orm import relationship


class Meeting(db.Model):
    __tablename__ = "Meeting"

    id = db.Column(db.Integer, primary_key=True)
    id_doctor = db.Column(db.String(128), db.ForeignKey("Doctor.id_pesel_num"))
    id_patient = db.Column(db.String(128), db.ForeignKey("Patient.id_pesel_num"))
    meeting_time = db.Column(db.DateTime, unique=False, nullable=True)
    meeting_description = db.Column(db.String(350), unique=False, nullable=True)

    def __init__(self, id_doctor, id_patient, meeting_time, meeting_description):
        self.id_doctor = id_doctor
        self.id_patient = id_patient
        self.meeting_time = meeting_time
        self.meeting_description = meeting_description
