from django import forms
from utils.django_forms import add_placeholder


class RecipeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add_placeholder(self.fields['username'], 'Type your username')
        # add_placeholder(self.fields['password'], 'Type your password')

    title = forms.CharField()
    description = forms.CharField()
    preparation_time = forms.IntegerField()
    preparation_time_unit = forms.CharField()
    servings = forms.IntegerField()
    servings_unit = forms.CharField()
    preparation_steps = forms.TextInput()
