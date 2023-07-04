from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_user, models_recipe

# GET Routes
# Route to take us the the add recipe page
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

# POST Routes