import pathlib
import uuid
import pint

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.urls import reverse

from main.utils import number_str_to_float

from food.models import Ingredient
from main.models import Unit

u2=pint.UnitRegistry()


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    servings = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)


    def get_calories(self):
        cals = 0
        ings = self.recipeingredient_set.all()
        for ing in ings:
            cals = cals + ing.ingredient.calorie * ing.as_grams()/self.servings
            print(type(cals))
        return cals


    def get_edit_url(self):
        return reverse("recipes:recipes-edit", kwargs={"id": self.id})

    def get_absolute_url(self):

        return reverse("recipes:recipes-detail", kwargs={"id": self.id})

class RecipeLine(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    directions = models.TextField(blank=True, null=True)

class LineIngredient(models.Model):
    recipeLine = models.ForeignKey(RecipeLine, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)




    quantity_as_float = models.FloatField(blank=True, null=True)
    # pounds, lbs, oz, gram, etc
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # unit = models.CharField(max_length=50, validators=[validate_unit_of_measure], blank=True, null=True)


    def get_absolute_url(self):
        return reverse("recipes:recipes-detail", kwargs={"id": self.id})




class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # recipe_id = models.AutoField -> ID to Recipe

    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50, )  # 1 1/4
    quantity_as_float = models.FloatField(blank=True, null=True)
    # pounds, lbs, oz, gram, etc
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # unit = models.CharField(max_length=50, validators=[validate_unit_of_measure], blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit.name.lower()]
        return measurement  # .to_base_units()

    def as_mks(self):
        # meter, kilogram, second
        measurement = self.convert_to_system(system='mks')
        return measurement.to_base_units()

    def as_grams(self):
        q=u2.Quantity


        va=q(self.quantity_as_float, self.unit.name)

        val=va.to('gram')

        return val.magnitude


    def as_imperial(self):
        # miles, pounds, seconds
        measurement = self.convert_to_system(system='imperial')
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)



    def get_absolute_url(self):
        return reverse("recipes:recipes-detail", kwargs={"id": self.id})





# TODO in the template if liquid unit uses crash converting in grams

"""
title = models.CharField(max_length=100, null=True)
shortname = models.CharField(max_length=10)
description = models.TextField(blank=True, default='')
date_created = models.DateTimeField(auto_now_add=True, null=True)
date_modify = models.DateTimeField(auto_now=True, null=True)
image = models.ImageField(        null=True)
platingimage = models.ImageField(null=True)
servings = models.IntegerField(default=1)
preptime = models.DurationField(blank=True, null=True)
# if i use semilavorati
preptimeUsingSemlav = models.DurationField(null=True, blank=True)
# how to cook it
cooking = models.TextField(blank=True, default='')
# cookingProgram = models.ForeignKey()
directions = models.TextField(blank=True, default='')
# where did you get it
origin = models.CharField(max_length=50, blank=True, null=True)
# nutritional intended for serving



"""

"""
class RecipeIngredient(models.Model):
recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='ingredients')
ingredient = models.ForeignKey(Recipe, on_delete=models.PROTECT, related_name='recipe')


"""

# class RecipeImage():
#     recipe = models.ForeignKey(Recipe)
