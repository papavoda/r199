# Generated by Django 4.1.5 on 2023-04-10 17:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0020_rename_created_contactus_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, verbose_name='Телефон'),
        ),
    ]