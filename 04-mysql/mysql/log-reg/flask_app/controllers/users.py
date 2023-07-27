from flask import render_template, redirect, session, request

from flask_app import app
from flask_app.models.user import User

# ! FAT MODELS THIN CONTROLLERS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/users/create', methods = ['POST'])
def register():
    print("❤️"*6,request.form,"❤️"*6)
    if User.validate_register(request.form):
        User.create(request.form)
        return redirect('/dashboard')
    return redirect('/')




        