## Synopsis

Travel app is aimed to give the user transparency in booking flights.  The user can choose a popular destination and compare what the flight costs to what it should cost. The user can also visually compare other popular cities' flight prices and recommendations. From there, the user can see local events for their selected city and notify themselves or their friends event information directly from the app . Travel App also provides a RESTful API for its' flight recommendations in JSON.  

![homepage](/static/homepage.jpg?raw=true "Optional Title")

![citypage](/static/citypage.jpg?raw=true "Optional Title")

![Eventpage](/static/eventPage.jpg?raw=true"Optional Title")

![Api](/static/apiPage.jpg?raw=true "Optional Title")


## Installation
Travel App requires a requirements.txt file installation. Travel app runs through the server.py file on http://localhost:5000/


## API Reference

Travel App runs on a local database. Estimated flight costs and flight booking recommendations are provdided by Sambre Api. Lowest fare for flights is provided by QPX (Google Flights API).  Since data is saved locally, Travel app flight recommendations are based on the departure date Sept 20, 2016 with the booking date as August 10, 2016. 

Data was saved locally to prevent API call expenses, and improve runtime. 

## Tests

Tests for Travel App are located in tests.py . Travel App offers 56% test coverage through unittests. Testing covers assertions on all pages on Travel App, and ensures that when a user selects a city the correct city information is displayed in flight recoemndations and event infomation 

Testing does not cover querying the database, hence the low percentage.


