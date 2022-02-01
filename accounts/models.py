from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField


class Account(models.Model):

    username = CharField(max_length=50, null=True, blank=True)
    password = CharField(max_length=50, null=True, blank=True)
    email = EmailField(null=True, blank=True)
