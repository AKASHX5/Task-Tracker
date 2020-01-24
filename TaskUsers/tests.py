from django.test import TestCase
import json
import base64
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# Create your tests here.

PASSWORD = "cft6"


def create_user(email='user@user.com', password=PASSWORD):
    return get_user_model().objects.create_user(
        email = email,
        password=password
    )


def test_user_can_log_in(self):

    user  = create_user()
    response = self.client.post(reverse('log_in'), data={
        'username': user.username,
        'password': 'cft6',
    })

    access = response.data['access']
    header, payload, signature = access.split('.')
    decoded_payload = base64.b64decode(f'{payload}==')
    payload_data = json.loads(decoded_payload)

    self.assertEqual(status.HTTP_200_OK,response.status_code)
    self.assertIsNotNone(response.data['refresh'])
    self.assertEqual(payload_data['id'], user.id)
    self.assertEqual(payload_data['username'],user.username)

