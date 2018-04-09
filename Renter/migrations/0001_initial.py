# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-22 01:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_animal', models.BooleanField(default=False)),
                ('is_smoker', models.BooleanField(default=False)),
                ('is_single', models.BooleanField(default=False)),
                ('job', models.CharField(max_length=225)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]