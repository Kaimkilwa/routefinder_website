# Generated by Django 2.2.6 on 2019-10-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20191025_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='serviceCtrFile/'),
        ),
    ]
