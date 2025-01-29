from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH,
            f'//input[@placeholder="{placeholder}"]'
        )

    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' '*20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')

        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')

        callback(form)

        return form

    def test_empty_first_name_error_message(self):

        def callback(form):

            first_name_field = self.get_by_placeholder(form, 'Type your first name')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('Write your first name', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):

        def callback(form):

            last_name_field = self.get_by_placeholder(form, 'Type your last name')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('Write your last name', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):

        def callback(form):

            username_field = self.get_by_placeholder(form, 'Type your username')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('This field must be not empty', form.text)
        self.form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):

        def callback(form):

            email_field = self.get_by_placeholder(form, 'Type your E-mail')
            for i in range(len(email_field.get_attribute("value"))):
                email_field.send_keys(Keys.LEFT)
                email_field.send_keys(Keys.DELETE)
            email_field.send_keys('test@test')
            email_field.send_keys(Keys.ENTER)

            form = self.get_form()
            self.assertIn('Valid E-mail is required', form.text)

        self.form_field_test_with_callback(callback)

    def test_password_do_not_match(self):

        def callback(form):

            password = self.get_by_placeholder(form, 'Type your password')
            password2 = self.get_by_placeholder(form, 'Repeat your password')
            password.send_keys('P@ssw0rd')
            password2.send_keys('P@ssw0rd_Different')
            password2.send_keys(Keys.ENTER)

            form = self.get_form()
            self.assertIn('Passwords must be equal', form.text)

        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Type your first name').send_keys('Testando')
        self.get_by_placeholder(form, 'Type your last name').send_keys('Teste')
        self.get_by_placeholder(form, 'Type your username').send_keys('testeuser')
        self.get_by_placeholder(form, 'Type your E-mail').send_keys('Testando@test.com')
        self.get_by_placeholder(
            form, 'Type your password').send_keys('P@ssw0rd')
        self.get_by_placeholder(
            form, 'Repeat your password').send_keys('P@ssw0rd')

        form.submit()

        self.assertIn('Your user is created, please log in',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
