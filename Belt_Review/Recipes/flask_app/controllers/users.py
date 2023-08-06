from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect('/')
    user = User.get_user_by_id(session)
    recipes = Recipe.get_all_recipes()
    return render_template('dashboard.html', user = user , recipes = recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/users/create', methods = ['POST'])
def create():
    # print(request.form)
    if User.validate(request.form):
        pw_hashed = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hashed)
        data = {
            **request.form,
            'password': pw_hashed,
        }
        user_id = User.create_user(data)
        session['id'] = user_id
        if user_id:
            flash("Registration Successful !", "registration")
        return redirect('/')
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    print(request.form)
    if User.login_validation(request.form):
        session['id'] = User.get_user_by_email(request.form).id
        return redirect('/dashboard')
    return redirect('/')