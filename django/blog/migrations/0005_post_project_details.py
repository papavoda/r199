from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('blog', '0004_alter_image_name')]
    operations = [
        migrations.AddField(model_name='post', name='project_area', field=models.DecimalField('Площадь объекта, м²', max_digits=8, decimal_places=1, null=True, blank=True)),
        migrations.AddField(model_name='post', name='project_location', field=models.CharField('Расположение объекта', max_length=150, blank=True)),
        migrations.AddField(model_name='post', name='project_duration', field=models.CharField('Срок выполнения', max_length=100, blank=True)),
        migrations.AddField(model_name='post', name='project_cost', field=models.DecimalField('Стоимость работ, ₽', max_digits=12, decimal_places=0, null=True, blank=True, help_text='Только подтверждённая стоимость выполненных работ, если её можно публиковать.')),
    ]
