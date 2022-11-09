from flask import render_template, request, url_for, redirect


def index():

    return redirect(url_for("blueprint.customers"))
