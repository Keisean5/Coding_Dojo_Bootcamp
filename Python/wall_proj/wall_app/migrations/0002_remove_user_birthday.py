# Generated by Django 2.2.4 on 2020-10-14 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
