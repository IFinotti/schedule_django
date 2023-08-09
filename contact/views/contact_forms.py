from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact

# Create your views here.
# When you make a instance of a form, you need to attach it to a model (in this
# case, the contact model).


def create(request):
    form_action = reverse('contact:create')
    # It shows the sent data if the method is POST
    if request.method == 'POST':
        form = ContactForm(data=request.POST, files=request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            "contact/create.html",
            context,
        )

    # If the method sent by the form is different of POST, the url shows the empty form
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    return render(
        request,
        "contact/create.html",
        context,
    )


def update(request, contact_id):
    # if it dont pass by the line below, it shows a 404 page
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    # If the method is post, the data just mantains there, and we sent the instance
    # to update the contact
    if request.method == 'POST':
        form = ContactForm(data=request.POST,
                           files=request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            "contact/create.html",
            context,
        )

    # If the method sent by the form is different of POST, the url shows the empty form
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    return render(
        request,
        "contact/create.html",
        context,
    )


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return (
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )
