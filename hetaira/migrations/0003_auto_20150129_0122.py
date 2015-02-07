# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hetaira', '0002_auto_20150129_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salt', models.CharField(max_length=128)),
                ('twilio_sid', models.CharField(max_length=128)),
                ('twilio_authtoken', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='InitialSalt',
        ),
    ]
