from flask import render_template, request, redirect,session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    session.clear()
    return redirect('/')

@app.route('/users/create', methods = ['POST'])
def create_user():
    if User.validate(request.form):
        user_id = User.create(request.form)
        session['id'] = user_id
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def get_users():
    if 'id' not in session:
        return redirect('/')
    
    users = User.get_all()
    one_user = User.get_one_by_id({'id':session['id']}) 
    return render_template('success.html', users = users , one_user = one_user)
    

@app.route('/destroy/<int:id>', methods=['POST'])
def destroy(id):
    User.destroy({'id':id})
    if id == session['id']:
        session.clear()
        return redirect('/')
    return redirect('/success')
