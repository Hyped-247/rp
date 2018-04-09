from django.db import models
from Apt.models import Apt
from Owner.models import Owner
from Worker.models import Worker


class Job(models.Model):
    owner = models.ForeignKey(Owner)
    worker = models.ForeignKey(Worker)
    apt = models.ManyToManyField(Apt)
    title = models.CharField(max_length=255)
    hours_week = models.IntegerField(default=30)
    price_per_hour = models.FloatField(default=10)
