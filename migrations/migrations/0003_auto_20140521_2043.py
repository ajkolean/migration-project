# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations

def change_field(apps, schema_editor):
    restaurant = apps.get_model('migrations', 'Restaurant')
    for r in restaurant.objects.all():
        r.derrscore_temp = r.derrscore
        r.save()


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0002_restaurant_derrscore_temp'),
    ]

    operations = [
        migrations.RunPython(change_field),
    ]
