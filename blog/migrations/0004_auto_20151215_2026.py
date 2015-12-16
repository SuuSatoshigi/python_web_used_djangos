# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151215_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
