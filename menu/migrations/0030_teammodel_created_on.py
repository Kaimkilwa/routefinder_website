# Generated by Django 2.2.6 on 2019-10-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0029_auto_20191028_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
