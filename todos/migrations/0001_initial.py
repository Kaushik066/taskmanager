# Generated by Django 2.0.2 on 2018-02-24 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank='true', default=datetime.datetime.now)),
            ],
        ),
    ]
