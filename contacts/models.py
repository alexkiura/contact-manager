"""Application models."""

from django.db import models


class Contact(models.Model):
    """Contact model."""
    name = models.CharField(max_length=250, blank=False)
    telephone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=254, blank=True, default='')
    nick_name = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.telephone_number)

class Person(models.Model):
    """Person model"""
    email = models.EmailField(max_length=254, blank=True, unique=True)
    name = models.CharField(max_length=255, blank=True)
