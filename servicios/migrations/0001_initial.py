# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('icono', models.ImageField(upload_to='servicios/')),
                ('imagen', models.ImageField(upload_to='servicios/')),
            ],
            options={
                'verbose_name_plural': 'servicios',
            },
            bases=(models.Model,),
        ),
    ]
