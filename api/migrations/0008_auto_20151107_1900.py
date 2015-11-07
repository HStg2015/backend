# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_objectsubcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleoffer',
            name='description',
            field=models.CharField(max_length=4096),
        ),
    ]
