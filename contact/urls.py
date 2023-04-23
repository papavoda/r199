from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path("contact_us/", views.ContactUs.as_view(), name='contact_us'),
    path('about/', views.AboutView.as_view(), name="about"),
    ]
