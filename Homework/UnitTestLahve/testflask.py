import unittest

from Flask import Flask


class TestFlask(unittest.TestCase):

    def test_initialization(self):
        flask = Flask(3.0)
        self.assertEqual(flask.capacity, 3.0)
        self.assertEqual(flask.volume, 0.0)
        self.assertTrue(flask.isclosed)  # Fix: is_closed -> isclosed

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Flask(6.0)
        with self.assertRaises(ValueError):
            Flask(0.4)
        with self.assertRaises(ValueError):
            Flask("3.0")

    def test_open_close_flask(self):
        flask = Flask(3.0)
        flask.open_flask()
        self.assertFalse(flask.isclosed)  # Fix: is_closed -> isclosed
        flask.close_flask()
        self.assertTrue(flask.isclosed)  # Fix: is_closed -> isclosed

    def test_set_volume_liters(self):
        flask = Flask(3.0)
        flask.open_flask()
        flask.set_volume(2.0)
        self.assertEqual(flask.get_volume(), 2.0)  # Fix: using get_volume()

    def test_set_volume_above_capacity(self):
        flask = Flask(3.0)
        flask.open_flask()
        flask.set_volume(4.0)
        self.assertEqual(flask.get_volume(), 3.0)  # Fix: using get_volume()

    def test_set_volume_ml(self):
        flask = Flask(3.0)
        flask.open_flask()
        flask.set_volume_ml(1500)
        self.assertEqual(flask.get_volume(), 1.5)  # Fix: using get_volume()

    def test_empty_flask(self):
        flask = Flask(2.0)
        flask.open_flask()
        flask.set_volume(1.0)
        flask.empty_the_flask()
        self.assertEqual(flask.get_volume(), 0.0)  # Fix: using get_volume()

    def test_closed_flask_exceptions(self):
        flask = Flask(2.0)
        with self.assertRaises(Exception):
            flask.set_volume(1.0)

    def test_invalid_volume(self):
        flask = Flask(3.0)
        flask.open_flask()
        with self.assertRaises(ValueError):
            flask.set_volume(-1.0)
        with self.assertRaises(ValueError):
            flask.set_volume("1.0")

if __name__ == '__main__':
    unittest.main()
