from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import recipe_list_view, recipe_detail_view, recipe_create_view, recipe_update_view, line_create_view, \
    recipe_line_view, recipe_active_list

app_name = 'recipes'

urlpatterns = [
    path('', recipe_list_view, name='recipes-list'),
    path('create/', recipe_create_view, name='recipes-create'),
    path('<int:id>/edit/', recipe_update_view, name='recipes-edit'),
    path('<int:id>/', recipe_detail_view, name='recipes-detail'),
    path('<int:id>/lines/', recipe_line_view, name='recipe-lines'),
    path('line/create/', line_create_view, name='line-create'),
    path('active', recipe_active_list, name='recipe-active-list'),


]
