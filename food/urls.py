from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import food_main_view, CategoryListView, impcat, imping, createIngredient

app_name='food'

urlpatterns = [
    path('', food_main_view, name='foodmain'),

    path('create_ing/', createIngredient, name='ingredient-create'),
    path('ing_import/', imping),
    path('cat_import/', impcat),




]
