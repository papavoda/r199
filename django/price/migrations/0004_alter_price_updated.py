# Generated by Django 4.1.5 on 2023-01-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_alter_price_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]