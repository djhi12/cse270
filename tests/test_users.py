import unittest
import requests


class TestUsersEndpoint(unittest.TestCase):
    base_url = 'http://127.0.0.1:8000/users/'

    def test_valid_credentials(self):
        url = self.base_url + '?username=admin&password=qwerty'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_invalid_credentials(self):
        url = self.base_url + '?username=admin&password=admin'
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
