from django.contrib import admin

from .models import Ingredient, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',


    ]



@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'amido',
        'calorie',
        'glucidi',
        'proteine',
        'lipidi',
        'amido',


    ]

