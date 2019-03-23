import sys
sys.path.insert(0, "../cap")
import utils_get_data
import unittest
from unittest.mock import patch



class TestGetData(unittest.TestCase):

    def test_connection(self):
        self.assertIsNotNone(utils_get_data.osm_requests('http://www.example.org'))

    def test_osm_requests(self):
        with patch('utils_get_data.requests.get') as get_mock:
            get_mock.return_value.ok = True
            get_mock.return_value.text = 'Succes'

            response = utils_get_data.osm_requests("Poznań")
            print(response.return_value)
            get_mock.assert_called_with('https://nominatim.openstreetmap.org/search/?', params={'q': 'Poznań', 'format': 'json', 'addressdetails': 1, 'limit': 1, 'polygon_svg': 1})
            self.assertEqual(response, 'Succes')



if __name__ == '__main__':
    unittest.main()
