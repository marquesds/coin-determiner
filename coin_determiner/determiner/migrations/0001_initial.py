# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.IntegerField(validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(1)], default=1, verbose_name='Value')),
            ],
            options={
                'verbose_name_plural': 'Coins',
                'verbose_name': 'Coin',
            },
        ),
    ]
