# Generated by Django 2.0.1 on 2018-02-11 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180210_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['spell']},
        ),
    ]