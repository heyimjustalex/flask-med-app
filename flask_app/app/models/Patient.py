from app.database.database import db
from sqlalchemy.orm import relationship


class Patient(db.Model):
    __tablename__ = "Patient"

    id_pesel_num = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=True)
    surname = db.Column(db.String(128), unique=False, nullable=True)
    email = db.Column(db.String(128), unique=False, nullable=True)
    phone_num = db.Column(db.String(64), unique=False, nullable=True)
    born = db.Column(db.DateTime, unique=False, nullable=True)
    address = db.Column(db.String(128), unique=False, nullable=True)
    disability = db.Column(db.Boolean, unique=False, nullable=True)
    medical_offer = db.Column(db.String(128), unique=False, nullable=True)
    meetings = relationship("Meeting")

    def __init__(
        self,
        id_pesel_num,
        name,
        surname,
        email,
        phone_num,
        born,
        address,
        disablity,
        medical_offer,
    ):
        self.id_pesel_num = id_pesel_num
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_num = phone_num
        self.born = born
        self.address = address
        self.disability = disablity
        self.medical_offer = medical_offer
