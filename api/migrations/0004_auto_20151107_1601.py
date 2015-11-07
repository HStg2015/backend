# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151107_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleoffer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 7, 15, 1, 7, 78805, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='simpleoffer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='api.UploadedFile/bytes/filename/mimetype'),
        ),
    ]
