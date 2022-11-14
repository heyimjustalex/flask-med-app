from app.database.database import db
from sqlalchemy.orm import relationship


class Doctor(db.Model):
    __tablename__ = "Doctor"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    pesel = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), unique=False, nullable=True)
    surname = db.Column(db.String(128), unique=False, nullable=True)
    email = db.Column(db.String(128), unique=False, nullable=True)
    phone_num = db.Column(db.String(64), unique=False, nullable=True)
    born = db.Column(db.DateTime, unique=False, nullable=True)
    address = db.Column(db.String(128), unique=False, nullable=True)
    disability = db.Column(db.Boolean, unique=False, nullable=True)
    medical_specialization = db.Column(db.String(128), unique=False, nullable=True)
    meetings = relationship("Meeting", lazy='select')

    def __init__(
        self,
        pesel,
        name,
        surname,
        email,
        phone_num,
        born,
        address,
        disablity,
        medical_specialization,
    ):
        self.pesel = pesel
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_num = phone_num
        self.born = born
        self.address = address
        self.disability = disablity
        self.medical_specialization = medical_specialization
