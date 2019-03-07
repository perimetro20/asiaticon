# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Container = apps.get_model('importing', 'Container')
    db_alias = schema_editor.connection.alias
    Container.objects.using(db_alias).bulk_create([
        Container(cbm=33.2, measurements='cnt 1 20"', ton=25, price=1900),
        Container(cbm=66.7, measurements='cnt 2 40"', ton=25, price=1850),
        Container(cbm=76.4, measurements='40" HQ', ton=25, price=1850),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Container = apps.get_model('importing', 'Container')
    db_alias = schema_editor.connection.alias
    Container.objects.using(db_alias).filter(cbm=33.2, measurements='cnt 1 20"', ton=25, price=1900).delete()
    Container.objects.using(db_alias).filter(cbm=66.7, measurements='cnt 2 40"', ton=25, price=1850).delete()
    Container.objects.using(db_alias).filter(cbm=76.4, measurements='40" HQ', ton=25, price=1850).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0010_container'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]