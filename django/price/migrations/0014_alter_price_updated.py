# Generated by Django 4.1.5 on 2023-01-29 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0013_alter_price_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 29, 18, 51, 37, 240551), null=True),
        ),
    ]