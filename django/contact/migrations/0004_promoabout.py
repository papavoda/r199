# Generated by Django 4.1.5 on 2023-01-16 16:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', ckeditor.fields.RichTextField(max_length=1000)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_promo', to='contact.about')),
            ],
        ),
    ]