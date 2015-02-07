# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hetaira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialSalt',
            fields=[
                ('salt', models.CharField(max_length=128, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='reportedentity',
            name='identifier',
            field=models.CharField(max_length=128, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
