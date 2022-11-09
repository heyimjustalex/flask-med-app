from flask import Blueprint
from app.controllers.mainController import *
from app.controllers.customerController import *


blueprint = Blueprint("blueprint", __name__)
blueprint.route("/", methods=["GET"])(index)
blueprint.route("/customers/")(customers)
blueprint.route("/customers/<int:id>/")(customer)
blueprint.route("/customers/add/", methods=["GET", "POST"])(customer_add)
blueprint.route("/customers/<int:id>/edit/", methods=["GET", "POST"])(customer_edit)
blueprint.route("/customers/<int:id>/delete/", methods=["GET", "POST"])(customer_delete)
