# Generated by Django 4.1.5 on 2023-01-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_about_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_hero_image',
            field=models.ImageField(default='', help_text='about_hero_image 1920x1280', upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='main_image',
            field=models.ImageField(default='', help_text='add main about img 1280x853', upload_to='about/'),
        ),
    ]