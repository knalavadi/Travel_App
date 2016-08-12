"""Models and database functions for Ratings project."""
import heapq
import time
from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

# class User(db.Model):
#     """User of ratings website."""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     email = db.Column(db.String(64), nullable=True)
#     password = db.Column(db.String(64), nullable=True)
#     age = db.Column(db.Integer, nullable=True)
#     zipcode = db.Column(db.String(15), nullable=True)

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return "<User user_id=%s email=%s>" % (self.user_id, self.email)

class City(db.Model):
    """Cities a user can visit."""

    __tablename__ = "cities"

    city_id = db.Column(db.String(64), autoincrement=True, primary_key=True)
    destination = db.Column(db.String(64), nullable=True )
    departure_date = db.Column(db.String(64), nullable=True)
    return_date = db.Column(db.String(64), nullable=True)
    lowest_predicted_fares=db.Column(db.String(64), nullable=True)
    lowest_fare=db.Column(db.String(64), nullable=True)
    recommendation = db.Column(db.String(15), nullable=True)
    coords = db.Column(db.String(64), nullable=True)
    # lat = db.Column(db.String(64), nullable=True)
    # lng = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "You should %s to book tickets to %s. The lowest predicted fare is $%s, and the lowest available fare is $%s" % (self.recommendation, self.destination, self.lowest_predicted_fares, self.lowest_fare)




# replace to events 
class Event(db.Model):
#     """Event info in cities."""

    __tablename__ = "events"

    city_id = db.Column(db.String(64), db.ForeignKey('cities.city_id'))
    event_id = db.Column(db.String(64), primary_key=True )
    destination = db.Column(db.String(64),nullable=True)
    event_date = db.Column(db.String(64), nullable=True)
    event_time = db.Column(db.String(64), nullable=True)   
    event_name = db.Column(db.String(64), nullable=True)   
    event_location = db.Column(db.String(64), nullable=True)   
    event_cost = db.Column(db.String(64), nullable=True)   
    event_theme = db.Column(db.String(64), nullable=True)       


#     # Defines relationship to cities
    city = db.relationship("City",
                           backref=db.backref("events", order_by=event_id))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<location %s name %s>" % (
            self.destination, self.event_name)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cities'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    import os
    os.system("dropdb cities")
    os.system("dropdb events")
    print 'droppping db'
    os.system("createdb cities")
    os.system("createdb events")
    print 'creatdb'
    from server import app
    connect_to_db(app)
    print "Connected to DB."
    db.create_all()
