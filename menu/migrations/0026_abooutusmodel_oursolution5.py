# Generated by Django 2.2.6 on 2019-10-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0025_auto_20191026_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='abooutusmodel',
            name='oursolution5',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
