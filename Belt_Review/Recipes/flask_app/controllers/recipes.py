from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User



@app.route('/recipes/new')
def new_recipe():
    if 'id' not in session:
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'id' not in session:
        return redirect('/')
    recipe = Recipe.get_recipe_by_id({'id':id})
    return render_template("edit_recipe.html" ,recipe= recipe)

@app.route('/recipes/update/<int:id>',methods = ['POST'])
def update_recipe(id):
    if Recipe.validate(request.form):
        print(request.form)
        data = {
            **request.form,
            'id':id
        }
        print(data)
        Recipe.update_recipe(data)
        return redirect('/dashboard')
    # return redirect('/recipes/edit/<int:id>')
    return redirect(url_for('edit_recipe', id=id))

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    print(request.form)
    if Recipe.validate(request.form):
        data = {
            **request.form,
            'user_id': session['id']
        }
        print(data)
        Recipe.create_recipe(data)
        return redirect('/dashboard')
    return redirect('/recipes/new')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'id' not in session:
        return redirect('/')
    recipe = Recipe.get_recipe_by_id({'id':id})
    user = User.get_user_by_id(session)
    return render_template("show_recipe.html", recipe = recipe, user = user)

@app.route('/delete/<int:id>', methods= ['POST'])
def destroy(id):
    if 'id' not in session:
        return redirect('/')
    Recipe.destroy({'id':id})
    return redirect('/dashboard')