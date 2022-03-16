import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        wichita_usa = city_country('wichita', 'usa')
        self.assertEqual(wichita_usa, 'Wichita, USA')


if __name__ == '__main__':
    unittest.main()