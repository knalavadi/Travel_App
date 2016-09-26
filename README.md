## Synopsis

Flightplan is a Python based Flask app aimed to give the user transparency in booking flights.  The user can choose a popular destination and compare the lowest flight fare to its actual definitve worth. The user can also visually compare other popular cities' flight prices and recommendations. From there, the user can see local events for their selected city and notify themselves or their friends event information directly from the app. Flightplan also provides a RESTful API for its' flight recommendations in JSON.  



![demo](/static/demo.gif?raw=true "demo")



## Installation
Flightplan requires a requirements.txt file installation. Flightplan runs through the server.py file on http://localhost:5000/


## API Reference

Flightplan runs on a Postgres database. Estimated flight costs and flight booking recommendations are provided by Sambre Api (https://developer.sabre.com/io-docs). Lowest fare for flights is provided by QPX (Google Flights API). Since data is saved locally, Flightplan's flight recommendations are based on the departure date Sept 20, 2016 with the booking date as August 10, 2016. 

Data was saved locally to prevent API call expenses, and improve runtime. 

## Tests

Tests for Flightplan are located in tests.py . Flightplan offers 56% test coverage through unittests. Testing covers assertions on all pages on Flightplan, and ensures that when a user selects a city the correct city information is displayed in flight recommendations and event infomation. 

Testing does not cover querying the database, hence the low percentage.

![coverageHTML](/static/coverage.jpg?raw=true "Testing Coverage")

## Tech Stack
Python, Javascript, JQuery, Jinja, SQL, SQLAlchemy, D3, HTML, CSS, Coverage 


