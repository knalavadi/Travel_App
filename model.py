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
    """User of ratings website."""

    __tablename__ = "cities"

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    destination = db.Column(db.String(64), nullable=True)
    departure_date = db.Column(db.String(64), nullable=True)
    return_date = db.Column(db.String(64), nullable=True)
    recommendation = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "You should %s to book tickets to %s" % (self.recommendation, self.destination)



# replace to events 
# class Rating(db.Model):
#     """Rating of a movie by a user."""

#     __tablename__ = "ratings"

#     rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     score = db.Column(db.Integer)

#     # Define relationship to user
#     user = db.relationship("User",
#                            backref=db.backref("ratings", order_by=rating_id))

#     # Define relationship to movie
#     movie = db.relationship("Movie",
#                             backref=db.backref("ratings", order_by=rating_id))

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
#             self.rating_id, self.movie_id, self.user_id, self.score)


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
    print 'droppping db'
    os.system("createdb cities")
    print 'creatdb'
    from server import app
    connect_to_db(app)
    print "Connected to DB."
    db.create_all()
