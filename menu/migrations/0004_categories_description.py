# Generated by Django 2.2.6 on 2019-10-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20191024_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
