from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [

    path('calc/', views.CalcView.as_view(), name="calc"),

]