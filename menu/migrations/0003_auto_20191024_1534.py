# Generated by Django 2.2.6 on 2019-10-24 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20191024_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='serviceename',
            new_name='servicename',
        ),
    ]
