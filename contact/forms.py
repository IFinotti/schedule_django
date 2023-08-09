from django.core.exceptions import ValidationError
from django import forms
from contact import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',

        )

    # Here you return the super and the clean. It can be used with more than one field at once

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first-name')
        last_name = cleaned_data.get('first-name')

        if first_name == last_name:
            msg = ValidationError(
                'The first name cannot be identic as the last name.',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    # In the clean_(field) you've to return the name of the field
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Do not type "ABC"',
                    code='invalid')
            )

        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'E-mail already exists.',
                    code='invalid'
                )
            )
        return email
