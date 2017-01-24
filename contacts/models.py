"""Application models."""

from django.db import models


class Contact(models.Model):
    """Contact model."""
    name = models.CharField(max_length=250, blank=False)
    telephone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=254, blank=True, default='')

    def __str__(self):
        return '{} {}'.format(self.name, self.telephone_number)
