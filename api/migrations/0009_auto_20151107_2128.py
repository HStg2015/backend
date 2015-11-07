# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20151107_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helptimesearch',
            name='email',
        ),
        migrations.AddField(
            model_name='helptimesearch',
            name='camp',
            field=models.ForeignKey(to='api.RefugeeCamp', default=1),
            preserve_default=False,
        ),
    ]
