# Generated by Django 4.1.5 on 2023-01-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_homeheroslogans_delete_smallpromoabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeheroslogans',
            name='text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]