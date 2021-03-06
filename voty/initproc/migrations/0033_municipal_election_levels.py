# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-26 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initproc', '0032_add_completed_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='ebene',
            field=models.CharField(choices=[('Bund', 'Bund'), ('Baden-Württemberg', 'Baden-Württemberg'), ('Bayern', 'Bayern'), ('Berlin', 'Berlin'), ('Brandenburg', 'Brandenburg'), ('Bremen', 'Bremen'), ('Hamburg', 'Hamburg'), ('Hessen', 'Hessen'), ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'), ('Niedersachsen', 'Niedersachsen'), ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'), ('Rheinland-Pfalz', 'Rheinland-Pfalz'), ('Saarland', 'Saarland'), ('Sachsen', 'Sachsen'), ('Sachsen-Anhalt', 'Sachsen-Anhalt'), ('Schleswig-Holstein', 'Schleswig-Holstein'), ('Thüringen', 'Thüringen'), ('Leinfelden-Echterdingen', 'Leinfelden-Echterdingen'), ('Stuttgart', 'Stuttgart'), ('Tübingen', 'Tübingen')], max_length=50),
        ),
    ]
