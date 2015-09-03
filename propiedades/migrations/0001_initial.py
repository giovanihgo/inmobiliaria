# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('clave', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('terreno', models.CharField(blank=True, max_length=100)),
                ('construccion', models.CharField(blank=True, max_length=100)),
                ('precio', models.IntegerField(blank=True, default=0)),
                ('renta', models.IntegerField(blank=True, default=0)),
                ('banos', models.FloatField(blank=True, default=0.0)),
                ('recamaras', models.FloatField(blank=True, default=0.0)),
                ('operacion', models.ForeignKey(to='propiedades.Operacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
