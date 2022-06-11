from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import food_main_view, CategoryListView, impcat, imping, createIngredient, category_detail_view, \
    ingredient_list, ingredient_detail_view, ingredient_active_list, ingredient_make_active, ingredient_make_inactive, \
    editIngredient

app_name='food'

urlpatterns = [
    path('', food_main_view, name='foodmain'),
    path('category/<int:id>', category_detail_view, name='category-datail'),
    path('ingredient/<int:id>', ingredient_detail_view, name='ingredient-detail'),
    path('ingredient/<int:id>/acitve', ingredient_make_active, name='ingredient-make-active'),
    path('ingredient/<int:id>/inacitve', ingredient_make_inactive, name='ingredient-make-inactive'),


    path('create_ing/', createIngredient, name='ingredient-create'),
    path('edit_ing/<int:id>/', editIngredient, name='ingredient-edit'),
    path('ingredients/', ingredient_list, name='ingredient-list'),
    path('ingredients/active', ingredient_active_list, name='ingredient-active-list'),

    # path('ing_import/', imping),
    # path('cat_import/', impcat),




]
