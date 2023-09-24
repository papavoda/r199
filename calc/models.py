from django.db import models
from price.models import Price


#  Подсчет расхода материала
#  0,140 кг на 1м2 при толщине 10мм
class Calc(models.Model):
    # Ссылка на вид работы и цену
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='calc')
    material = models.CharField(max_length=150, verbose_name='Название материала')  #
    amount = models.DecimalField(verbose_name='Расход', max_digits=6, decimal_places=2)  # --> 0,140
    unit = models.CharField(max_length=30, default='кг', verbose_name='Единицы измерения')  # Ед. изм --> кг
    dimension = models.CharField(max_length=10, default='м²', verbose_name='Площадь/Объем')  # Площадь м2
    thickness = models.IntegerField(default=0, null=True, blank=True, verbose_name='Толщина слоя (мм)')  # --> мм
    boxing = models.IntegerField(default=20, null=True, blank=True)

    # переменные внешнего ключа
    def get_price(self):
        return self.price.objects.all()

    def __str__(self):
        return f'{self.material} - {self.price.category.name}'


class CalcSquare(models.Model):
    # Простое (например прямоугольная комната)
    # Сложное (эркер, коридор неправильной формы итп)
    # Default parameters (мм)
    room_type = models.CharField(max_length=20)
    room_type_description = models.CharField('Описание помещения', max_length=500, default='Простое/Сложное')
    perimetr = models.PositiveIntegerField(verbose_name='Периметр помещения', default=7300,)
    length = models.PositiveIntegerField(verbose_name='Длина помещения', default=5200, )
    width = models.PositiveIntegerField(verbose_name='Ширина помещения', default=3400)
    height = models.PositiveIntegerField(verbose_name='Высота помещения', default=2600)
    # Default windows/doors size (мм):
    door_width = models.PositiveIntegerField(verbose_name='Ширина двери', default=800)
    door_height = models.PositiveIntegerField(verbose_name='Высота двери', default=2000)
    window_width = models.PositiveIntegerField(verbose_name='Ширина окна', default=1550)
    window_height = models.PositiveIntegerField(verbose_name='Высота окна', default=1450)

    def __str__(self):
        return f'{self.room_type} - {self.room_type_description}'