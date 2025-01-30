from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from django.urls import reverse

import pytest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):

    def test_user_valid_data_can_login_successfully(self):
        string_password = 'P@ssw0rd1'
        user = User.objects.create_user(username='testeuser', password=string_password)

        # opened the login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User can see forms
        form = self.browser.find_element(
            By.CLASS_NAME,
            'main-form'
        )

        # User can select fields and type your credentials
        username_field = self.get_by_placeholder(form, 'Type your username')
        username_field.send_keys(user.username)
        password_field = self.get_by_placeholder(form, 'Type your password')
        password_field.send_keys(string_password)

        # User submit login credentials
        form.submit()

        # User can see succesfully login message
        self.assertIn('You are logged in', self.browser.find_element(
            By.TAG_NAME, 'body').text)

    def test_login_create_raises_404_if_not_post_method(self):
        self.browser.get(self.live_server_url + reverse('authors:login_create'))

        self.assertIn(
            'Not Found',
            self.browser.find_element(
                By.TAG_NAME, 'body').text
        )
