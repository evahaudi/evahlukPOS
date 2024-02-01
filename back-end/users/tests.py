from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

class SignupAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = '/api/signup/'

    def test_chef_signup(self):
        data = {
            'username': 'chefuser',
            'email': 'chef@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
            'fullname': 'Chef Full Name',
            'date_of_birth': '1990-01-01',
            'location': 'Chef Location',
            'experience_years': 5,
            'phone': '1234567890',
            'department': 'Chef Department',
            'role': 'Chef',
        }

        response = self.client.post(f'{self.signup_url}chef/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['role'], 'Chef')

    def test_manager_signup(self):
        data = {
            'username': 'manageruser',
            'email': 'manager@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
            'fullname': 'Manager Full Name',
            'date_of_birth': '1980-01-01',
            'location': 'Manager Location',
            'experience_years': 8,
            'phone': '9876543210',
            'department': 'Manager Department',
            'role': 'Manager',
        }

        response = self.client.post(f'{self.signup_url}manager/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['role'], 'Manager')

    def test_waiter_signup(self):
        data = {
            'username': 'waiteruser',
            'email': 'waiter@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
            'fullname': 'Waiter Full Name',
            'date_of_birth': '1985-01-01',
            'location': 'Waiter Location',
            'experience_years': 3,
            'phone': '5555555555',
            'department': 'Waiter Department',
            'role': 'Waiter',
        }

        response = self.client.post(f'{self.signup_url}waiter/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['role'], 'Waiter')

    def test_invalid_signup(self):
        data = {
            'username': 'invaliduser',
            'email': 'invalid@example.com',
            'password': 'testpassword',
            'password2': 'differentpassword',  # Mismatched password
            'fullname': 'Invalid User',
            'role': 'Chef',
        }

        response = self.client.post(f'{self.signup_url}chef/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_username_email(self):
        # Create a user first
        existing_user = get_user_model().objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpassword',
            fullname='Existing User',
            role='Chef',
        )

        data = {
            'username': 'existinguser',
            'email': 'existing@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
            'fullname': 'Duplicate User',
            'role': 'Chef',
        }

        response = self.client.post(f'{self.signup_url}chef/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_retrieval(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
            'fullname': 'Test Full Name',
            'date_of_birth': '1990-01-01',
            'location': 'Test Location',
            'experience_years': 5,
            'phone': '1234567890',
            'department': 'Test Department',
            'role': 'Chef',
        }

        response = self.client.post(f'{self.signup_url}chef/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        token_response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', token_response.data)
        self.assertIn('refresh', token_response.data)


    def test_password_mismatch(self):
        data = {
            'username': 'mismatchuser',
            'email': 'mismatch@example.com',
            'password': 'testpassword',
            'password2': 'mismatchedpassword',
            'fullname': 'Mismatch Full Name',
            'date_of_birth': '1990-01-01',
            'location': 'Mismatch Location',
            'experience_years': 5,
            'phone': '1234567890',
            'department': 'Mismatch Department',
            'role': 'Chef',
        }

        response = self.client.post(f'{self.signup_url}chef/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_invalid_endpoint(self):
        response = self.client.get('/api/signup/invalid/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

