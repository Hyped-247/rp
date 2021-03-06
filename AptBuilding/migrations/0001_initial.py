# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-14 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(default='Zanesville', max_length=225)),
                ('state', models.CharField(default='Zanesville', max_length=225)),
                ('zip_code', models.CharField(default='43701', max_length=5)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.Owner')),
            ],
        ),
    ]
