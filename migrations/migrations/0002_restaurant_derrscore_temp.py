# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='derrscore_temp',
            field=models.FloatField(default=2.0),
            preserve_default=False,
        ),
    ]
