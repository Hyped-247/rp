from django.db import models

from Apt.models import Apt
from Owner.models import Owner
from Renter.models import Renter


class Contract(models.Model):
    owner = models.ForeignKey(Owner)
    renter = models.ForeignKey(Renter)
    apt = models.ForeignKey(Apt)
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_process = models.CharField(max_length=255)
    price = models.FloatField(default=700)
    deposit = models.FloatField(default=500)

