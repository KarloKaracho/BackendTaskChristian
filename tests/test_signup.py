#~/movie-bag/tests/test_signup.py

import json

from tests.BaseCase import BaseCase


class SignupTest(BaseCase):

    def test_successful_signup(self):
        # Given
        email = "testuser@web.de"
        password = "mycoolpassword"

        payload = json.dumps({
            "email": email,
            "password": password
        })

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

