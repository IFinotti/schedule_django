from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Shows these fields in the top of the DB
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "show",
    )

    # Create a filter option
    list_filter = ("created_date",)

    # Sort contacts backwards based on id
    ordering = ("-id",)

    # A way to search the fields of any contact
    search_fields = (
        "id",
        "first_name",
        "last_name",
    )

    # Maximum of contacts in a single page
    list_per_page = 10

    # Limits the "Show all" option
    list_max_show_all = 100

    # Set these fields as editable at the index of DB
    list_editable = (
        "first_name",
        "last_name",
        "show",
    )

    # Clicking on these, it takes you to the info about the contact
    list_display_links = ("id", "phone")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("-id",)
