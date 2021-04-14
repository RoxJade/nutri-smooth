import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """Iterates through recipe data in MongoDB and returns recipes.html"""
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Register and check for existing username #
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Iterates though user data collection to check for exisiting
    username in MongoDB, if found it returns user to register.html
    with flash notification.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        """
        Inserts requested data into MongoDB and uses a hash
        method on user password when storing.
        """
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get(
                "password"))
            }
        mongo.db.users.insert_one(register)

        """Stores user's registration in session cookies and directs
        the user to their profile"""
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Sign in, checks for existing username, incorrect username/password #
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome to Nutri-Smooth, {}".format(
                        request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            flash("Incorrect Username and or/Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


# User Profile #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """returns user profile page @param username"""
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("signin"))


@app.route("/logout")
def logout():
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_smoothie", methods=["GET", "POST"])
def add_smoothie():
    """
    Function to allow a registered user to insert a new smoothie
    recipe onto the site and pulls the data through to MongoDB,
    then redirects the user back to the get_recipes function.
    """
    if request.method == "POST":
        is_favourite = "on" if request.form.get(
            "is_favourite") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_macros": request.form.get("recipe_macros"),
            "health_benefits": request.form.get("health_benefits"),
            "image_url": request.form.get("image_url"),
            "is_favourite": is_favourite,
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your smoothie has been added!")
        return redirect(url_for("get_recipes"))

    """
    Get categories from MongoDB to pull through into category dropdown options
    """
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_smoothie.html", categories=categories)


@app.route("/edit_smoothie/<recipe_id>", methods=["GET", "POST"])
def edit_smoothie(recipe_id):
    """
    Function to allow a registered user to edit and save edited
    recipe onto the site and pulls the data through to MongoDB,
    then redirects the user back to the edit_smoothie page.
    """
    if request.method == "POST":
        is_favourite = "on" if request.form.get(
            "is_favourite") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_macros": request.form.get("recipe_macros"),
            "health_benefits": request.form.get("health_benefits"),
            "image_url": request.form.get("image_url"),
            "is_favourite": is_favourite,
            "created_by": session["user"]
        }
        mongo.db.recipes.update(
            {"_id": ObjectId(recipe_id)}, submit)
        flash("Your smoothie recipe has been updated!")

    """
    Target the individual recipe selected by user for
    editing using the Object Id in MongoDB
    """
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_smoothie.html", recipe=recipe, categories=categories)


@app.route("/delete_smoothie/<recipe_id>")
def delete_smoothie(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Smoothie recipe deleted")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
