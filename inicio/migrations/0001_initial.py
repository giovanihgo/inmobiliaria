# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('telefono', models.CharField(max_length=50)),
                ('movil', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('logo', models.ImageField(upload_to='general/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('seo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
