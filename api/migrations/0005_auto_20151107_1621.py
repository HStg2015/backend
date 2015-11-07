# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151107_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='simpleoffer',
            name='category',
            field=models.ForeignKey(null=True, to='api.ObjectCategory'),
        ),
    ]
