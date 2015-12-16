# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('project_name', models.TextField()),
                ('project_scaffold_text', models.TextField()),
                ('project_self_function', models.TextField()),
                ('project_skill', models.TextField()),
                ('project_url', models.TextField()),
                ('project_cut', models.TextField()),
                ('is_project_show', models.BooleanField()),
                ('project_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
