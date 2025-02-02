# Generated by Django 2.2.6 on 2019-11-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekers', '0005_auto_20191118_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='highest_qualification',
            field=models.CharField(choices=[('DE', 'Deploma'), ('BA', 'Bachelor')], max_length=200),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='nationality',
            field=models.CharField(choices=[('AL', 'Algeria'), ('AN', 'Angola')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekersmodel',
            name='years_of_exprience',
            field=models.CharField(choices=[('three', '3year'), ('no', 'No exprience'), ('one', '1year'), ('four', '3year')], max_length=200),
        ),
    ]
