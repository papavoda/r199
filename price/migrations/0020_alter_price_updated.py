# Generated by Django 4.1.5 on 2023-03-26 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0019_alter_price_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 12, 10, 32, 666823), null=True),
        ),
    ]