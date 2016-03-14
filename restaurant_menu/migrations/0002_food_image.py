# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.CharField(default=b'none.jpgs', max_length=150),
            preserve_default=True,
        ),
    ]
