from django.contrib.auth.models import User
from django.db import models


class Worker(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    skill = models.CharField(max_length=300)

