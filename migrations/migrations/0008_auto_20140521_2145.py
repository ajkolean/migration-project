# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0007_auto_20140521_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='menu',
            new_name='website',
        ),
    ]
