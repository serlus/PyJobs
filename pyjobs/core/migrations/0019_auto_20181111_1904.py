# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-11 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0018_messages_message_type")]

    operations = [
        migrations.AlterField(
            model_name="messages",
            name="message_title",
            field=models.CharField(
                default="", max_length=100, verbose_name="Título da Mensagem"
            ),
        ),
        migrations.AlterField(
            model_name="messages",
            name="message_type",
            field=models.CharField(
                default="offer",
                max_length=200,
                verbose_name="Ticker usado no backend para ID da msg",
            ),
        ),
    ]
