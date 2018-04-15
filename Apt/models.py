from django.db import models
from AptBuilding.models import AptBuilding


class Apt(models.Model):
    aptBuilding = models.ForeignKey(AptBuilding)
    number = models.IntegerField(default=0)
    allow_smocking = models.BooleanField(default=False)
    room_num = models.IntegerField(default=4)

    def __str__(self):
        return "Apt num: " + str(self.number)

