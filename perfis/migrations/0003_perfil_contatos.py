# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(related_name='_perfil_contatos_+', to='perfis.Perfil'),
        ),
    ]
