from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.exceptions import ValidationError
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact import models


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
