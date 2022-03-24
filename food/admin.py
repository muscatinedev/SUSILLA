from django.contrib import admin

from .models import Ingredient, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',

    ]
    prepopulated_fields = {'slug': ('name',)}


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
        'slug',

    ]
    prepopulated_fields = {'slug': ('name',)}
