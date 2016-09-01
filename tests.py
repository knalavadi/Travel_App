import unittest

from server import app
from model import db, example_data, connect_to_db



class CityTests(unittest.TestCase):
    """Tests for flight booking site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

#tests homepage:
    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("Where to?:", result.data)

#tests example london city page:
    def test_city_page(self):
        result = self.client.post("/city_page",
                                 data={'city':"London"}, 
                                 follow_redirects=True)
        self.assertNotIn("events for you", result.data)

#tests example london event page:
    def test_city_event_page(self):
        result = self.client.post("/city_event_page/London",
                                  data={'city': "London"},
                                  follow_redirects=True)
        self.assertNotIn(" compare to other popular destintations out of SFO", result.data)

#tests api page
    def test_api(self):
        result = self.client.get("/api")
        self.assertIn("RESTful API using Python and Flask", result.data)

#tests example london json file:
    def test_api_city(self):
        result = self.client.get("api/v1.0/cities/<int:city_id>",
                                  data={'city': "London"},
                                  follow_redirects=True)
        self.assertNotIn(" compare to other popular destintations out of SFO", result.data)


#tests all cities api json file:
    def test_api_all_cities(self):
        result = self.client.get("/api/v1.0/cities")
        self.assertIn('estimated fare',result.data)    





class CityTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()
