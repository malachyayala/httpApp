# Generated by Django 3.2.16 on 2022-11-14 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221113_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='userId',
        ),
    ]
