# Generated by Django 2.0.4 on 2019-02-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0012_auto_20181219_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importresponse',
            name='time_production',
            field=models.IntegerField(verbose_name='Production Time(days)'),
        ),
    ]
