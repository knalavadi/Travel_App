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
    # destination = get key from get request
    destination = request.form['destination']
    print "DESTINATION ", destination

    city = City.query.filter_by(destination=destination).first()
    print city
    flash(city)

    return render_template("city_page.html", city=city)




# # ==============================city event page===========
@app.route('/city_event_page/<destination>', methods=['GET'])
def city_page(destination):

    # print destination
    destination = City.query.filter_by(destination=destination).first()
    print destination
    # print destination.events
    # print "DESTINATION event page", destination 
    flash(destination)

    return render_template("city_event_page.html", events=destination.events, city_event_destination=destination)






if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
