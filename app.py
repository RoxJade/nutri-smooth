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
@app.route("/index")
def index():
    """Function returns home page"""
    return render_template("index.html")


@app.route("/get_recipes")
def get_recipes():
    """Iterates through recipe data in MongoDB and returns recipes.html"""
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Function to search Mongo database using index, returns search for
    any 'text' existing in category name, recipe name and recipe ingredients"""
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Iterates though user data to check for exisiting
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
        Inserts requested user data into MongoDB and uses a hash
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

        """
        Stores user's registration in session cookies and directs
        the user to their profile.
        """
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    """
    Search database for user data to sign in, checks for incorrect name or
    password and redirects user to their profile.
    """
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
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Returns user profile page @param username"""
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    """
    Returns all recipes to admin profile and returns recipes
    created by user to user profile.
    """
    if session["user"]:
        if session["user"] == "admin":
            own_recipes = list(mongo.db.recipes.find())
        else:
            own_recipes = list(mongo.db.recipes.find(
                {"created_by": session["user"]}))
        return render_template(
            "profile.html", username=username, own_recipes=own_recipes)

    return redirect(url_for("signin"))


@app.route("/logout")
def logout():
    """
    Remove user session cookies for user to log out.
    """
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_smoothie", methods=["GET", "POST"])
def add_smoothie():
    """
    Allow registered user to post new smoothie
    data on site and database, then redirects
    user back to the smoothies page.
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
    Get categories from MongoDB to appear in categories dropdown selection
    on 'add_smoothie' page.
    """
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_smoothie.html", categories=categories)


@app.route("/edit_smoothie/<recipe_id>", methods=["GET", "POST"])
def edit_smoothie(recipe_id):
    """
    Allow registered user to target their added recipes for editing,
    using recipe object_id, save edit on site and post to database.
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
    Target individual recipe selected by user for
    editing using the Object Id in MongoDB.
    """
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_smoothie.html", recipe=recipe, categories=categories)


@app.route("/delete_smoothie/<recipe_id>")
def delete_smoothie(recipe_id):
    """
    Delete an individual smoothie recipe from site and
    MongoDB targeting user's recipe Object_Id.
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Smoothie recipe deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    """
    Get list of categories from MongoDB and sort alphabetically.
    Return list to categories page.
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Add new smoothie category to site and MongoDB,
    restricted to admin user only.
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New smoothie category added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Allow admin user to edit and save smoothie categories, using
    Object_Id, on site and post to database, then redirect
    to 'edit_category' page.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Your edit has been saved")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one(
        {"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Allow admin user to delete a chosen smoothie category
    targeting Object_Id, on site and database, then redirect
    the user back to the categories page.
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Smoothie category deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
