# Generated by Django 3.1.7 on 2021-03-23 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0009_auto_20210323_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='slug',
        ),
    ]
