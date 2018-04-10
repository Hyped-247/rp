from django.contrib.auth.models import User
from django.db import models


class Owner(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=225, default="Zanesville")
    state = models.CharField(max_length=225, default="Zanesville")
    zip_code = models.CharField(max_length=5, default="43701")

    def __str__(self):
        return self.user.get_full_name()