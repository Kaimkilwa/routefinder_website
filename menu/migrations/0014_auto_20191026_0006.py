# Generated by Django 2.2.6 on 2019-10-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_auto_20191025_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='categoryfile',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
