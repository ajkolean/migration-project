# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0004_remove_restaurant_derrscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='derrscore_temp',
            new_name='derrscore',
        ),
    ]
