# Generated by Django 2.0.4 on 2018-10-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0004_client_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='importrequest',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]