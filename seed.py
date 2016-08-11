"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime

from model import City, connect_to_db, db
from server import app






def load_cities():
    """Load users from u.user into database."""

    print "City"

    for row in open("seed_data/u.flight_data"):
        row = row.rstrip()
        
        city_id, origin_location, destination, departure_date, return_date, highest_predicted_fares, currency_code, lowest_predicted_fares, recommendation, lowest_fare = row.split("|")

        city = City(destination=destination,
                    departure_date=departure_date,
                    return_date=return_date,
                    recommendation=recommendation,
                    )

        # We need to add to the session or it won't ever be stored
        db.session.add(city)

        # provide some sense of progress
    
    # Once we're done, we should commit our work
    db.session.commit()



# def load_events():
    



if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    load_cities()
