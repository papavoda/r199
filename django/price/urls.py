from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [

    path('price/', views.PriceView.as_view(), name="price"),



]