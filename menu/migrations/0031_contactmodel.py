# Generated by Django 2.2.6 on 2019-10-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0030_teammodel_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(blank=True, max_length=200, null=True)),
                ('customeremail', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=200, max_length=200, null=True)),
                ('massege', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
