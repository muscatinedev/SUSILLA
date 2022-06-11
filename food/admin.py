from django.contrib import admin

from .models import Ingredient, Category, IngredientStock


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

admin.site.register(IngredientStock )
