from django.shortcuts import render

import datetime

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from .models import Price, PriceCategory

# https://docs.djangoproject.com/en/4.1/topics/http/views/


class PriceView(TemplateView):
    model = Price
    template_name = 'price/price.html'
    context_object_name = 'price_list'  # имя в шаблоне
    # queryset = Price.objects.select_related('category').all()

    def get_context_data(self, **kwargs):
        context = super(PriceView, self).get_context_data()
        context['main_title'] = 'цены'
        # доп функция в шаблон
        # context['price_cats'] = PriceCategory.objects.all()

        context['prices'] = Price.objects.select_related('category').all()
        context['price_cats'] = PriceCategory.objects.all()

        return context


class CalcView(TemplateView):
    template_name = 'price/calc.html'

    def get_context_data(self, **kwargs):
        context = super(CalcView, self).get_context_data()
        context['main_title'] = 'Калькулятор'
        context['nbar'] = 'calc'
        return context
