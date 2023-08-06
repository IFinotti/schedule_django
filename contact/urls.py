from django.urls import path
from contact import views

app_name = "contact"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),

    # contacts urls crud
    path("contact/<int:contact_id>/", views.contact, name="contact"),
    # path("contact/<int:contact_id>/update/", views.contact, name="contact"),
    # path("contact/<int:contact_id>/delete/", views.contact, name="contact"),
    # path("contact/create/", views.contact, name="contact"),
]
