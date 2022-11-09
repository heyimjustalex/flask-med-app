from app import app
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship
from app.database.database import db
from app.models.Meeting import Meeting
from app.models.Patient import Patient
from app.models.Doctor import Doctor
from app.models.Medical_interview import Medical_interview
from datetime import datetime

# from app.routes.routes import blueprint


def setup_database():
    with app.app_context():
        db.drop_all()
    with app.app_context():
        db.create_all()
        db.session.commit()
    with app.app_context():

        db.session.add(
            Patient(
                id_pesel_num="123231312",
                name="jack",
                surname="sparrow",
                email="asd@asd.pl",
                phone_num="790231432",
                born=datetime.strptime("Jun 1 2005", "%b %d %Y"),
                address="asdasd",
                disablity=1,
                medical_offer="test",
            )
        )
        db.session.add(
            Patient(
                id_pesel_num="132131231",
                name="jack2",
                surname="sparrow2",
                email="asd2@asd.pl",
                phone_num="791231432",
                # born=datetime.strptime("Jun 3 2006 1:33PM", "%b %d %Y %I:%M%p"),
                born=datetime.strptime("Jun 3 2006", "%b %d %Y"),
                address="asdsadasd",
                disablity=0,
                medical_offer="test1",
            )
        )

        db.session.add(
            Patient(
                id_pesel_num="132132344",
                name="jack3",
                surname="sparrow3",
                email="asd3@asd.pl",
                phone_num="711232312",
                born=datetime.strpdate("May 12 2015", "%b %d %Y"),
                address="asdplplplpl",
                disablity=0,
                medical_offer="test2",
            )
        )

        db.session.add(
            Doctor(
                id_pesel_num="1233132344",
                name="jack3Doctor",
                surname="sparrow3Doctor",
                email="asd4@asd.pl",
                phone_num="7asd232312",
                born=datetime.strpdate("May 13 2015", "%b %d %Y"),
                address="asdplplplpl",
                disablity=0,
                medical_specialization="cardio",
            )
        )

        db.session.add(
            Doctor(
                id_pesel_num="18932344",
                name="jack4Doctor",
                surname="sparrow34Doctor",
                email="asd5@asd.pl",
                phone_num="7aasgg232312",
                born=datetime.strpdate("May 16 2015", "%b %d %Y"),
                address="asdplplplpasssl",
                disablity=1,
                medical_specialization="dentist",
            )
        )

        db.session.commit()


app = Flask(__name__, template_folder="app/templates")
app.config.from_object("app.config.Config")
db.init_app(app)
# app.register_blueprint(blueprint, url_prefix="/")
migrate = Migrate(app, db)
setup_database()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


# def configure_dependencies(binder):
#     binder.bind(SQLAlchemy, to=db, scope=flask_injector.singleton)

# flask_injector.FlaskInjector(app=app, modules=[configure_dependencies])
# print("DONE")
