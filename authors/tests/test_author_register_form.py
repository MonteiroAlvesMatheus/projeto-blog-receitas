from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorRegisterUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'Type your first name'),
        ('last_name', 'Type your last name'),
        ('username', 'Type your username'),
        ('email', 'Type your E-mail'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_fields_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', (
            'Mandatory. 150 characters or less. '
            'Letters, numbers and @/./+/-/_ only.')),
        ('email', 'The e-mail must be valid'),
        ('password', (
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters')),
    ])
    def test_fields_help_text_is_correct(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    @parameterized.expand([
        ('first_name', 'First Name'),
        ('last_name', 'Last Name'),
        ('username', 'Username'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('password2', 'Password Confirmation'),
    ])
    def test_fields_label_is_correct(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)
