from django.shortcuts import render

from contact.forms import ContactForm

# Create your views here.


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
