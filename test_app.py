# test_app.py

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up Flask app for testing."""
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        """Test the hello_world route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, Pop!')

if __name__ == '__main__':
    unittest.main()
