from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def create(request):
    search = request.POST.get('first_name')

    context = {

    }
    return render(
        request,
        "contact/create.html",
        context,
    )
