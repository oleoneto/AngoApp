# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_auto_20180302_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='tipo_de_servico',
            field=models.CharField(default='Geral ', max_length=50),
        ),
    ]