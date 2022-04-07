from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import recipe_list_view, recipe_detail_view, recipe_create_view, recipe_update_view

app_name='recipes'

urlpatterns = [
    path('', recipe_list_view, name='recipes-list'),
    path('<int:id>/', recipe_detail_view, name='recipes-detail'),
    path('create', recipe_create_view, name='recipes-create'),
    path('<int:id>/edit/', recipe_update_view, name='recipes-edit'),
    ]



