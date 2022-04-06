from django.contrib import admin

from main.models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = [
        'name',


    ]

