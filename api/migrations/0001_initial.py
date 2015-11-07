# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefugeeCamp',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('city', models.CharField(max_length=64)),
                ('postcode', models.CharField(max_length=16)),
                ('street', models.CharField(max_length=128)),
                ('streetnumber', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=64)),
                ('telnr', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
    ]
