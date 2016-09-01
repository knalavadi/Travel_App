"""City"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, City
import coverage
import doctest
# from functools import wrap 

app = Flask(__name__)

app.secret_key = "ABC"

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
    city = City.query.filter_by(destination=destination).first()
    return render_template("city_page.html", city=city)


# ==============================city event page===========
@app.route('/city_event_page/<destination>', methods=['GET'])
def city_page(destination):
    """ event page for selected city"""
    destination = City.query.filter_by(destination=destination).first()
    return render_template("city_event_page.html", events=destination.events, city_event_destination=destination)


# ==============================API Routes=========================================
@app.route('/api', methods=['GET', 'POST'])
def api_page():
    """api page, allows user to make GET request, renders information in JSON format """
    return render_template("api.html")



cities = [
    {
        'id': 1,
        'name': u'Los Angeles',
        'recomendation': u'Buy', 
        'estimated fare': '$105',
        'lowest fare': '$65'
    },
        {
        'id': 2,
        'name': u'Honolulu',
        'recomendation': u'Wait', 
        'estimated fare': '$379',
        'lowest fare': '$471'
    },
    {
        'id': 3,
        'name': u'Denver',
        'recomendation': u'Buy', 
        'estimated fare': '$97',
        'lowest fare': '$69'
    },
        {
        'id': 4,
        'name': u'Seattle',
        'recomendation': u'Buy', 
        'estimated fare': '$113',
        'lowest fare': '$84'
    },
        {
        'id': 5,
        'name': u'New York City',
        'recomendation': u'Buy', 
        'estimated fare': '$301',
        'lowest fare': '$179'
    },
        {
        'id': 6,
        'name': u'Phoenix',
        'recomendation': u'Wait', 
        'estimated fare': '$28',
        'lowest fare': '$64'
    },
        {
        'id': 7,
        'name': u'Miami',
        'recomendation': u'Buy', 
        'estimated fare': '$199',
        'lowest fare': '$163'
    },
        {
        'id': 8,
        'name': u'Portland',
        'recomendation': u'Buy', 
        'estimated fare': '$98',
        'lowest fare': '$79'
    },
        {
        'id': 9,
        'name': u'Las Vegas',
        'recomendation': u'Buy', 
        'estimated fare': '$59',
        'lowest fare': '$52'
    },
        {
        'id': 10,
        'name': u'Chicago',
        'recomendation': u'Wait', 
        'estimated fare': '$44',
        'lowest fare': '$54'
    },
        {
        'id': 11,
        'name': u'San Diego',
        'recomendation': u'Buy', 
        'estimated fare': '$127',
        'lowest fare': '$74'
    },
        {
        'id': 12,
        'name': u'San Antonio',
        'recomendation': u'Wait', 
        'estimated fare': '$253',
        'lowest fare': '$364'
    },
        {
        'id': 13,
        'name': u'Santa Barbara',
        'recomendation': u'Wait', 
        'estimated fare': '$148',
        'lowest fare': '$449'
    },
        {
        'id': 14,
        'name': u'New Orleans',
        'recomendation': u'Buy', 
        'estimated fare': '$273',
        'lowest fare': '$176'
    },
        {
        'id': 15,
        'name': u'Atlanta',
        'recomendation': u'Buy', 
        'estimated fare': '$215',
        'lowest fare': '$186'
    },
        {
        'id': 16,
        'name': u'Charleston',
        'recomendation': u'Buy', 
        'estimated fare': '$350',
        'lowest fare': '$187'
    },
        {
        'id': 17,
        'name': u'Charlotte',
        'recomendation': u'Buy', 
        'estimated fare': '$377',
        'lowest fare': '$302'
    },
        {
        'id': 18,
        'name': u'Washingotn DC',
        'recomendation': u'Buy', 
        'estimated fare': '$300',
        'lowest fare': '$209'
    },
        {
        'id': 19,
        'name': u'Philadelphia',
        'recomendation': u'Wait', 
        'estimated fare': '$293',
        'lowest fare': '$792'
    },
        {
        'id': 20,
        'name': u'Cleveland',
        'recomendation': u'Wait', 
        'estimated fare': '$242',
        'lowest fare': '$317'
    },
        {
        'id': 21,
        'name': u'Baltimore',
        'recomendation': u'Buy', 
        'estimated fare': '$342',
        'lowest fare': '$235'
    },
        {
        'id': 22,
        'name': u'Dallas',
        'recomendation': u'Wait', 
        'estimated fare': '$100',
        'lowest fare': '$105'
    },
        {
        'id': 23,
        'name': u'Austin',
        'recomendation': u'Buy', 
        'estimated fare': '$216',
        'lowest fare': '$151'
    },
        {
        'id': 24,
        'name': u'Boston',
        'recomendation': u'Wait', 
        'estimated fare': '$275',
        'lowest fare': '$189'
    },
        {
        'id': 25,
        'name': u'Houston',
        'recomendation': u'', 
        'estimated fare': '$98',
        'lowest fare': '$79'
    },
]

@app.route('/api/v1.0/cities', methods=['GET', 'POST'])
def get_tasks():
    """ route for api call to all cities"""
    return jsonify({'cities': cities})


@app.route('/api/v1.0/cities/<int:city_id>', methods=['GET', 'POST'])
def get_task(city_id):
    """ route for api call to selected cities"""
    city = [city for city in cities if city['id'] == city_id]
    return jsonify({'city': city[0]})

@app.route('/testing')
def testing_page():
    """ testing page"""
    return render_template("index.html")


#  =========================================
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')