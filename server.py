"""City"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, City
# from functools import wrap 

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")




# ==============================city page================

@app.route('/city_page', methods=['GET', 'POST'])
def city():
    # location = get key from get request
    destination = request.form['destination']
    print "DESTINATION ", destination

    destination = City.query.filter_by(destination=destination).all()
    flash(destination)


    # recommendation = City.query.filter_by(destination=destination).first()
    # flash("you should %s" % recommendation)



    # city = City.query.filter(City.destination == destination).first()
    # recommendation = City.query.filter(City.recommendation == recommendation).first()

    return render_template("city_page.html", destination=destination)




# # ==============================city event page===========
# @app.route('/city_event_page')
# def city_page():

#   return render_template("city_event_page.html")


# ======================login and logout for user ====================


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/login', methods=['POST'])

def login_process():
    """Process login."""
    error = None
    # Get form variables
    email = request.form["email"]
    password = request.form["password"]


    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect("/users/%s" % user.user_id)


@app.route('/logout')
# @login_required
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")



# =================register form ================

@app.route('/register', methods=['GET'])
def register_form():
    """Renders template only."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Redirects to homepage after submission for registered users."""

    email = request.form.get("email")
    print "EMAIL ", email
    password = request.form.get("password")

    user = User.query.filter(User.email == email).first()
    print "USER ", user

    if user == None:
        user = User(email=email, password=password)
        print "HERE"
        db.session.add(user)
        db.session.commit()
        session["user"] = email
        return redirect("/")

    elif User.password == password:
        session["user"] = email #keeps track of who logged in
        flash("Successfully logged in.")
        return redirect("/")

    else:
        flash("Password is incorrect.")
        return redirect('/register')

    return render_template("base.html")







if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
