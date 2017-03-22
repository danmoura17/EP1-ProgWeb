# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('email', models.EmailField(max_length=254)),
                ('filhos', models.IntegerField()),
            ],
        ),
    ]
