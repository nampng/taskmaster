# Generated by Django 3.2.3 on 2021-06-05 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210603_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routine',
            old_name='routine_time',
            new_name='time',
        ),
    ]