# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-08 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_markup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markupfield',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_markup_markupfield', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='markupfield',
            name='markup',
            field=models.CharField(choices=[('creole', 'Creole'), ('html', 'Pure HTML'), ('markdown', 'Markdown'), ('textile', 'Textile'), ('restructuredtext', 'ReST (ReStructured Text)')], max_length=20, verbose_name='Markup'),
        ),
    ]
