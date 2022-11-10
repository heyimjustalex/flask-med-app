from flask import render_template, request, url_for, redirect


def index():
    return render_template("index.html")
