# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_helptimesearch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectSubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('parent', models.ForeignKey(to='api.ObjectCategory')),
            ],
        ),
    ]
