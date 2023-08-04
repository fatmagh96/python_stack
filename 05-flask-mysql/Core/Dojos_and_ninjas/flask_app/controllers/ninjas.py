from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, redirect, request


@app.route('/ninjas')
def ninja_form():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos = dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')
