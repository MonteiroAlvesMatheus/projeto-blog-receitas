from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_attr, add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your username')
        add_placeholder(self.fields['email'], 'Type your E-mail')
        add_placeholder(self.fields['first_name'], 'Type your first name')
        add_placeholder(self.fields['last_name'], 'Type your last name')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    username = forms.CharField(
        label='Username',
        help_text=((
            'Mandatory. 150 characters or less. '
            'Letters, numbers and @/./+/-/_ only.')),
        error_messages={
            'required': 'This field must be not empty',
            'min_length': 'The username must have at least 4 characters',
            'max_length': 'The username must have less then 150 characters'
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First Name'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last Name'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        required=True,
        label='E-mail',
        help_text=('The e-mail must be valid'),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        label='Password',
        validators=[strong_password]

    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Password Confirmation'
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]
        # exemple:
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'placeholder': 'Type your first name',
        #         'class': 'input text-input'
        #     }),
        #     'password': forms.PasswordInput(attrs={
        #         'placeholder': 'Type your password here',
        #     })
        # }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Passwords must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
