# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-22 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Worker', '0001_initial'),
        ('Owner', '0001_initial'),
        ('Apt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hours_week', models.IntegerField(default=30)),
                ('price_per_hour', models.FloatField(default=10)),
                ('apt', models.ManyToManyField(to='Apt.Apt')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.Owner')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Worker.Worker')),
            ],
        ),
    ]
