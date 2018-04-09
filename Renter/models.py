from django.contrib.auth.models import User
from django.db import models


class Renter(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    has_animal = models.BooleanField(default=False)
    is_smoker = models.BooleanField(default=False)
    is_single = models.BooleanField(default=False)
    job = models.CharField(max_length=225)

