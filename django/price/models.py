from django.db import models
import datetime
from django.template.defaultfilters import slugify

from blog.models import Post  # import Post from blog to


class PriceCategory(models.Model):
    class Meta:
        ordering = ('pk',)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Price(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    # num = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE, related_name='price')
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL, related_name='price')
    dimension = models.CharField(max_length=10, default='м²')
    use_in_calc = models.BooleanField(default=False, help_text='Использ в калькуляторе', )
     # Поле для ручной сортировки внутри категории
    # Поле для ручной сортировки с плавающей точкой
    position = models.FloatField(
        default=0.0,
        verbose_name='Позиция',
        help_text='Число для порядка сортировки (меньше = выше). Можно использовать дроби для точной вставки между элементами.'
    )

    class Meta:
        # ordering = ('pk',)
        ordering = ['category', 'position', 'name']  # Сортировка по категории, затем по позиции, затем по имени
        # unique_together = ['category', 'position']  # Опционально: уникальная позиция в пределах категории

    # переменные внешнего ключа
    def get_price_categories(self):
        return self.category.objects.all()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Автоматическая установка позиции если не указана
        if self.position == 0.0:
            last_item = Price.objects.filter(
                category=self.category
            ).order_by('-position').first()
            self.position = (last_item.position + 1.0) if last_item else 1.0
        super().save(*args, **kwargs)

    def get_next_position(self):
        """Возвращает следующую позицию для категории"""
        last_item = Price.objects.filter(
            category=self.category
        ).order_by('-position').first()
        return (last_item.position + 1.0) if last_item else 1.0

    def move_to_position(self, new_position):
        """Перемещает элемент на указанную позицию, сдвигая другие при необходимости"""
        from django.db.models import F
        import math
        
        # Если позиция занята, сдвигаем все последующие элементы
        if Price.objects.filter(category=self.category, position=new_position).exists():
            Price.objects.filter(
                category=self.category, 
                position__gte=new_position
            ).update(position=F('position') + 1.0)
        
        self.position = new_position
        self.save()

# class Material(models.Model):
#     name = models.CharField(max_length=100)  # rotband
#     ru_name = models.CharField(max_length=300)  # Ротбанд (гипсовая штукатурка)
#     amount = models.DecimalField(max_digits=4, decimal_places=2)   # 8,5
#     unit = models.CharField(max_length=30, default='кг/м2')  # единица измерения например кг/м2
#     thickness = models.PositiveSmallIntegerField(default='10')  # толщина слоя мм
#
#
# class Calc(models.Model):
#     name = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='calc_name')
#     amount = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='calc_amount')
