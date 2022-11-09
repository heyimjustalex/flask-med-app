from flask import render_template, request, url_for, redirect
from app.models.customer import Customer
from app.database.database import db
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import asc

# getall
def customers():
    customers = Customer.query.order_by(asc("id"))
    return render_template("index.html", customers=customers)


# getbyid
def customer(id):
    customer = Customer.query.get_or_404(id)
    return render_template("customer.html", customer=customer)


# create user
def customer_add():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        surname = request.form["surname"]
        age = int(request.form["age"])
        customer = Customer(
            email=email,
            name=name,
            surname=surname,
            age=age,
        )
        db.session.add(customer)
        db.session.commit()

        return redirect(url_for("blueprint.customers"))
    else:
        return render_template("add_customer.html")


# update customer
def customer_edit(id):
    customer = Customer.query.get_or_404(id)
    if request.method == "POST":

        name = request.form["name"] if request.form["name"] != "" else customer.name
        surname = (
            request.form["surname"]
            if request.form["surname"] != ""
            else customer.surname
        )
        email = request.form["email"] if request.form["email"] != "" else customer.email

        try:
            age = int(request.form["age"])
        except:
            age = customer.age

        customer.email = email
        customer.name = name
        customer.surname = surname
        customer.age = age

        db.session.add(customer)
        db.session.commit()

        return redirect(url_for("blueprint.customers"))
    else:
        return render_template("edit_customer.html", customer=customer)


# delete customer
def customer_delete(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("blueprint.customers"))
