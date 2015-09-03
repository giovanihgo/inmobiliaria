# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='galeria/')),
                ('seo', models.CharField(max_length='100')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
