from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthorLogoutTest(TestCase):
    def get_user_login(self):
        password1 = 'pass'
        user = User.objects.create_user(username='testeuser', password=password1)

        self.client.login(
            username=user.username,
            password=password1
        )
        return user

    def test_author_logout_request_not_post(self):

        self.get_user_login()

        url_logout = reverse('authors:logout')
        response_logout = self.client.get(url_logout)
        url = response_logout.url

        self.assertIn('/authors/login/', url)

    def test_author_try_logout_other_username(self):

        self.get_user_login()

        logout_user = {
            'username': 'fulano',
            'password': 'pass'
        }

        url_logout = reverse('authors:logout')
        response_logout = self.client.post(url_logout, data=logout_user, follow=True)

        self.assertIn(
            'Invalid logout request',
            response_logout.content.decode('utf-8')
        )

    def test_author_logout_successfully(self):

        user = self.get_user_login()

        logout_user = {
            'username': 'testeuser',
            'password': 'pass'
        }

        url_logout = reverse('authors:logout')
        response_logout = self.client.post(url_logout, data=logout_user, follow=True)

        self.assertIn(
            'You have logged out successfully.',
            response_logout.content.decode('utf-8')
        )
