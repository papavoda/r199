# Generated by Django 4.1.5 on 2023-01-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_about_about_hero_image_alter_about_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='icon',
            field=models.FileField(blank=True, default='', null=True, upload_to='icons/social'),
        ),
    ]