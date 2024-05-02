# from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class CalcView(TemplateView):
    template_name = 'spa/index.html'

    def get_context_data(self, **kwargs):
        context = super(CalcView, self).get_context_data()
        context['main_title'] = 'Калькулятор ремонта'
        context['nbar'] = 'calc'
        return context