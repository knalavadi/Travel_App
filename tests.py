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
