# Generated by Django 4.1.5 on 2023-04-15 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0024_alter_price_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 20, 0, 4, 789731), null=True),
        ),
    ]