# Generated by Django 3.1.7 on 2021-03-28 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_feed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 3, 28), null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 3, 28), null=True),
        ),
    ]
