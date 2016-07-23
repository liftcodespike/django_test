# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='logreg.User')),
                ('user_poked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.User')),
            ],
            options={
                'db_table': 'pokes',
            },
        ),
    ]