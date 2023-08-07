from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
# Create your views here.


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()


def create(request):
    # It shows the sent data if the method is POST
    if request.method == 'POST':
        context = {
            'form': ContactForm(data=request.POST)
        }

        return render(
            request,
            "contact/create.html",
            context,
        )

    # If the method sent by the form is different of POST, the url shows the empty form
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        "contact/create.html",
        context,
    )
