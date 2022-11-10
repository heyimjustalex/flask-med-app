from flask import Blueprint
from app.controllers.mainController import *
from app.controllers.patientController import *
from app.controllers.doctorController import *


blueprint = Blueprint("blueprint", __name__)
blueprint.route("/", methods=["GET"])(index)

blueprint.route("/patients/", methods=["GET", "POST"])(patients)
blueprint.route("/patients/<int:id>/")(patient)
blueprint.route("/patients/add/")(patient_add)
blueprint.route("/patients/<int:id>/edit/", methods=["GET", "POST"])(patient_edit)
blueprint.route("/patients/<int:id>/delete/", methods=["GET", "POST"])(patient_delete)

blueprint.route("/doctors/", methods=["GET", "POST"])(doctors)
blueprint.route("/doctors/<int:id>/")(doctor)
blueprint.route("/doctors/add/")(doctor_add)
blueprint.route("/doctors/<int:id>/edit/", methods=["GET", "POST"])(doctor_edit)
blueprint.route("/doctors/<int:id>/delete/", methods=["GET", "POST"])(doctor_delete)
