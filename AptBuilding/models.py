from django.db import models
from Owner.models import Owner


class AptBuilding(models.Model):
    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length=225)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=225, default="Zanesville")
    state = models.CharField(max_length=225, default="Zanesville")
    zip_code = models.CharField(max_length=5, default="43701")
