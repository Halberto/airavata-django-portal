# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('template_type', models.IntegerField(choices=[(1, 'Verify Email Template'), (2, 'New User Email Template')], primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
