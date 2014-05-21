# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('healthiness', models.IntegerField(default=1, choices=[(0, b'Healthy'), (1, b'Average'), (2, b'Unhealthy')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('type', models.ForeignKey(to='migrations.Food', to_field='id')),
                ('daysopen', models.TextField()),
                ('derrscore', models.IntegerField(default=2, choices=[(0, b'Terrible'), (1, b'Bad'), (2, b'Average'), (3, b'Good'), (4, b'Amazing')])),
                ('location', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
