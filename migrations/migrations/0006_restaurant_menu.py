# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0005_auto_20140521_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
