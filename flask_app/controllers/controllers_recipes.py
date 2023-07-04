from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_user, models_recipe

# GET Routes
# Route to take us the the add recipe page.
@app.route('/new/recipe')
def new_recipe():
    print("Add recipe route...")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    print("Add recipe route successful...")
    return render_template('add_recipe.html', user=models_user.User.get_by_id(data))

# Route to take us to the edit recipe page.
@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    print("Edit recipe route...")
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    print("Edit recipe route successful...")
    return render_template('edit_recipe.html', edit=models_recipe.Recipe.get_one_recipe(data),
    user=models_user.User.get_by_id(user_data))

# POST Routes
@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    print("Creating new recipe route...")
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_recipe.Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        # cook_time must come back as an integer.
        "cook_time": int(request.form['cook_time']),
        "date_made": request.form['date_made'],
        "user_id": request.form['user_id']
    }
    models_recipe.Recipe.save_recipe(data)
    print("Recipe created successfully...")
    return redirect('/recipes')