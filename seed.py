"""Utility file to seed ratings database from city data in flight_data and event_data/"""

import datetime

from model import City, Event, connect_to_db, db
from server import app



def load_cities():
    """Load users from u.user into database.
    >>> load_cities()
    City
"""

    print "City"

    for row in open("seed_data/u.flight_data"):
        row = row.rstrip()
        print row.split("|")        

        city_id, origin_airport, destination_airport, destination, departure_date, return_date, highest_predicted_fares, currency_code, lowest_predicted_fares, recommendation, lowest_fare, destination_info  = row.split("|")

        city = City(city_id=city_id,
                    origin_airport=origin_airport,
                    destination_airport=destination_airport,
                    destination=destination,
                    departure_date=departure_date,
                    return_date=return_date,
                    lowest_predicted_fares=lowest_predicted_fares,
                    lowest_fare=lowest_fare,
                    recommendation=recommendation,
                    destination_info=destination_info,
                    )

        # We need to add to the session or it won't ever be stored
        db.session.add(city)

        # provide some sense of progress
    
    # Once we're done, we should commit our work
    db.session.commit()



def load_events():

    print "Event"
    for row in open("seed_data/u.event_data"):
        row = row.rstrip()
        print row.split("|")

        city_id, event_id, destination, event_date, event_time, event_name, event_location, event_cost, event_theme, event_description = row.split("|")

        event = Event(city_id=city_id,
                    event_id=event_id,
                    destination=destination,
                    event_date=event_date,
                    event_time=event_time,
                    event_name=event_name,
                    event_location=event_location,
                    event_cost=event_cost,
                    event_theme=event_theme,
                    event_description=event_description
                    )

        # Add to the session 
        db.session.add(event)

        # provide some sense of progress
    
    # Once we're done, we should commit our work
    db.session.commit()                             



if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    load_cities()
    load_events()
