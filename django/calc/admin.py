from django.contrib import admin
from .models import Calc, CalcSquare


@admin.register(CalcSquare)
class CalcSquareAdmin(admin.ModelAdmin):
    list_per_page = 10



@admin.register(Calc)
class CalcAdmin(admin.ModelAdmin):
    list_per_page = 10
    # list_display = ['pk', 'price', 'material', 'amount', 'unit', 'dimension', 'thickness', 'boxing']
