"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime

from model import City, Event, connect_to_db, db
from server import app



def load_cities():
    """Load users from u.user into database."""

    print "City"

    for row in open("seed_data/u.flight_data"):
        row = row.rstrip()
        print row.split("|")        

        # add : lat, lng 
        
        city_id, origin_location, destination, departure_date, return_date, highest_predicted_fares, currency_code, lowest_predicted_fares, recommendation, lowest_fare, coords = row.split("|")

        city = City(city_id=city_id,
                    destination=destination,
                    departure_date=departure_date,
                    return_date=return_date,
                    lowest_predicted_fares=lowest_predicted_fares,
                    lowest_fare=lowest_fare,
                    recommendation=recommendation,
                    coords = coords
                    # lat=lat,
                    # lng=lng
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

        city_id, event_id, destination, event_date, event_time, event_name, event_location, event_cost, event_theme = row.split("|")

        event = Event(city_id=city_id,
                    event_id=event_id,
                    destination=destination,
                    event_date=event_date,
                    event_time=event_time,
                    event_name=event_name,
                    event_location=event_location,
                    event_cost=event_cost,
                    event_theme=event_theme,
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
