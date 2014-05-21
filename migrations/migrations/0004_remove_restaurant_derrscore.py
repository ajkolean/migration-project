# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0003_auto_20140521_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='derrscore',
        ),
    ]
