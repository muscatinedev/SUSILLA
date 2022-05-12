from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import food_main_view, CategoryListView, impcat, imping, createIngredient, category_detail_view

app_name='food'

urlpatterns = [
    path('', food_main_view, name='foodmain'),
    path('category/<int:id>', category_detail_view, name='category-datail'),


    path('create_ing/', createIngredient, name='ingredient-create'),
    # path('ing_import/', imping),
    # path('cat_import/', impcat),




]
