# Generated by Django 4.1.5 on 2023-01-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_alter_price_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='num',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]