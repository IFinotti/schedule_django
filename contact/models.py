from django.db import models
from django.utils import timezone


class Contact(models.Model):

    # User data
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, blank=True)

    # optional description
    # It shows when the user was created and a description about it
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    # Apply the first and last name as the field who shows each contact
    # __str__ method overwrite that field described above
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
