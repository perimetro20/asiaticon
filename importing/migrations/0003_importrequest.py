# Generated by Django 2.0.4 on 2018-10-08 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0002_client_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000, verbose_name='Product Name')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('aeroshipment', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='importing.Client')),
            ],
        ),
    ]
