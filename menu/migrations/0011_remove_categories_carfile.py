# Generated by Django 2.2.6 on 2019-10-25 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20191025_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='carfile',
        ),
    ]
