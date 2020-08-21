# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('host_name', models.CharField(max_length=200)),
                ('host_ip', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'hosts',
            },
        ),
        migrations.CreateModel(
            name='Host_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='host_type',
            field=models.ForeignKey(to='mhosts.Host_type'),
        ),
    ]
