# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=100)),
                ('os_type', models.CharField(max_length=20, default='windows')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('host_name', models.CharField(max_length=50)),
                ('host_ip', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_pass', models.CharField(max_length=50)),
                ('group', models.ForeignKey(to='mhosts.Group')),
            ],
            options={
                'verbose_name_plural': 'hosts',
            },
        ),
    ]
