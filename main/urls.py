from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import main_view

app_name='main'

urlpatterns = [
    path('',  main_view, name='main-view'),




]
