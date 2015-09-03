# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=150)),
                ('comentario', models.TextField()),
                ('avatar', models.ImageField(upload_to='comentarios/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
