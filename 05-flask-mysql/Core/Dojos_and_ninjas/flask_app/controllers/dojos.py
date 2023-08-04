from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, redirect, request

@app.route('/dojos')
def index():
    all_dojos = Dojo.get_all_dojos()
    return render_template("index.html",all_dojos = all_dojos)

@app.route('/')
def reroute():
    return redirect('/dojos')

@app.route('/dojos/create', methods=['POST'])
def create():
    data_dict = request.form
    Dojo.create_dojo(data_dict)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def get_ninjas(id):
    dojo = Dojo.get_all_ninjas_in_dojo(id)
    # if not dojo:
    #     return redirect('/')
    # else:
    return render_template("display.html", dojo = dojo)
