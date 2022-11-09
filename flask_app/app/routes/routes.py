from flask import Blueprint
from app.controllers.mainController import *
from app.controllers.patientController import *


blueprint = Blueprint("blueprint", __name__)
blueprint.route("/", methods=["GET"])(index)
blueprint.route("/patients/")(patients)
blueprint.route("/patients/<int:id>/")(patient)
blueprint.route("/patients/add/", methods=["GET", "POST"])(patient_add)
blueprint.route("/patients/<int:id>/edit/", methods=["GET", "POST"])(patient_edit)
blueprint.route("/patients/<int:id>/delete/", methods=["GET", "POST"])(patient_delete)
