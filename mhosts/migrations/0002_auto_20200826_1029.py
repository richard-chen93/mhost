# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mhosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='os_type',
            field=models.CharField(max_length=20, default='windows'),
        ),
        migrations.AlterField(
            model_name='group',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
