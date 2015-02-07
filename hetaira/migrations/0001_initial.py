# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedEntity',
            fields=[
                ('identifier', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('vi', models.IntegerField()),
                ('np', models.IntegerField()),
                ('hg', models.IntegerField()),
                ('ns', models.IntegerField()),
                ('nc', models.IntegerField()),
                ('dr', models.IntegerField()),
                ('po', models.IntegerField()),
                ('st', models.IntegerField()),
                ('ph', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
