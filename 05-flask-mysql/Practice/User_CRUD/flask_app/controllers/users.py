from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User 
# from datetime import datetime



@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def read():
    all_users = User.get_all()
    return render_template('index.html', all_users = all_users)

@app.route('/users/new')
def add():
    return render_template('new_user_form.html')

@app.route('/user/create', methods = ['POST'])
def create():
    print(request.form)
    data_dict = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print("+++++", data_dict, "++++++" )
    User.create(data_dict)
    return redirect('/users')

@app.route('/users/<int:id>')
def show(id):
    user = User.get_user_by_id(id)
    return render_template("show.html", user = user)

@app.route('/users/<int:id>/edit')
def edit(id):
    user = User.get_user_by_id(id)
    return render_template('update.html', user = user)

@app.route('/users/<int:id>/update', methods = ['POST'])
def update(id):
    data_dict = {
            **request.form,
            'id' : id
        }
    User.update(data_dict)
    return redirect('/')

@app.route('/users/<int:id>/delete', methods=['POST'])
def delete(id):
    User.delete(id)
    return redirect('/')