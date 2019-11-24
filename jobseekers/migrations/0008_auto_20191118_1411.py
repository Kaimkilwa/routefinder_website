# Generated by Django 2.2.6 on 2019-11-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekers', '0007_auto_20191118_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseekersmodel',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='jobseekersmodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='nationality',
            field=models.CharField(choices=[('AL', 'Algeria'), ('AN', 'Angola')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='years_of_exprience',
            field=models.CharField(choices=[('three', '3year'), ('one', '1year'), ('no', 'No exprience'), ('four', '3year')], max_length=200),
        ),
    ]
