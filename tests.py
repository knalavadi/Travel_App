import unittest

from server import app
from model import db, example_data, connect_to_db


class CityTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("Where to?:", result.data)

    def test_city_page(self):
        result = self.client.get("/city_page")
        self.assertIn(" compare to other popular destintations out of SFO", result.data)
        self.assertNotIn("events for you", result.data)

    def test_city_event_page(self):
        result = self.client.post("/city_event_page/Charleston",
                                  data={'city': "Charleston"},
                                  follow_redirects=True)
        self.assertIn("Charleston events for you", result.data)
        self.assertIn("Whiskey After Dark", result.data)
        self.assertNotIn(" compare to other popular destintations out of SFO", result.data)


class PartyTestsDatabase(unittest.TestCase):
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
