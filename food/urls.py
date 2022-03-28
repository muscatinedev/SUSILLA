from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import food_main_view

app_name='food'

urlpatterns = [
    path('', food_main_view, name='foodmain'),
   # path('create_category', createCategory, name='create-category')


]
