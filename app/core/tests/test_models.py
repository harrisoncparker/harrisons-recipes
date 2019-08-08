from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'name@test.com'
        password = 'TestPass123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test that the new user emails are case insensitive """
        email = 'NAME@Test.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='TestPass123!'
        )

        self.assertEqual(user.email, 'name@test.com')

    def test_new_user_invalid_email(self):
        """ Test the validation on the user model """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='password'
            )
