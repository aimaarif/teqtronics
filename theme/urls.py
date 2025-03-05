from django.contrib import admin
from django.urls import path
from theme import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contactform/', views.contactform, name='contactform'), 
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('services/', views.services, name='services'),
    path('search/', views.search, name='search'),
]
