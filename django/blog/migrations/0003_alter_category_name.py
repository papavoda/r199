# Generated by Django 5.2 on 2025-05-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_meta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Название категории', max_length=100),
        ),
    ]
