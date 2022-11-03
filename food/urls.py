from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import food_main_view, category_list_view, category_detail_view, ingredient_detail_view, \
    ingredient_make_active, ingredient_make_inactive, createIngredient, editIngredient, ingredient_active_list, \
    ingredients_main_view, IngredientiList

app_name='food'

urlpatterns = [
    path('', food_main_view, name='food-main'),

    path('ingredients/', ingredients_main_view, name='ingredient-main'),



    path('category/', category_list_view, name='category-list'),
    path('category/<int:id>', category_detail_view, name='category-datail'),

    path('ingredient/<int:id>', ingredient_detail_view, name='ingredient-detail'),
    path('ingredient/<int:id>/acitve', ingredient_make_active, name='ingredient-make-active'),
    path('ingredient/<int:id>/inacitve', ingredient_make_inactive, name='ingredient-make-inactive'),


    path('create_ing/', createIngredient, name='ingredient-create'),
    path('edit_ing/<int:id>/', editIngredient, name='ingredient-edit'),

    path('ingredients/active', ingredient_active_list, name='ingredient-active-list'),




    # path('ing_import/', imping),
    # path('cat_import/', impcat),




]

htmx_urlpatterns = [
    path('check_ingname/', views.check_ingname, name='check_ingname'),
    path('add-ingredient/', views.add_ing, name='add-ing'),
    path('delete_ingredient/<int:pk>', views.del_ing, name='delete-ingredient'),
    path('ingredient/category<int:pk>', views.cat_ing_list, name='get-cat-ingredients'),



]
urlpatterns +=htmx_urlpatterns
