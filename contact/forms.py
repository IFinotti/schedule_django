from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.exceptions import ValidationError
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-a class-b',
                'placeholder': 'Here is the third way.'
            }
        ),
        # label='Primeiro nome finotti',
        help_text='A help text.'
    )

    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class-a class-b',
    #         'placeholder': 'Write your name here.'
    #     })

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class-a class-b',
        #             'placeholder': 'Write your name here.'
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code='invalid'
        #     )
        # )

        return super().clean()
