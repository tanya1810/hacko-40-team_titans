# Generated by Django 3.0.7 on 2021-03-27 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 3, 27), null=True),
        ),
    ]
