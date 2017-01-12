from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    telephone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)
