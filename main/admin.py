from django.contrib import admin

from main.models import Unit, Task


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = [
        'name',


    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'name',


    ]
