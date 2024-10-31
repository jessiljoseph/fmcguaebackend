from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

class User(AbstractUser):
    country = CountryField(blank_label='(select country)', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
