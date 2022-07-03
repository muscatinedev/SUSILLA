from django.db import models
from django.urls import reverse

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class IngredientStock(models.Model):
    quantity_as_float = models.FloatField(blank=True, null=True)
    min_quantity_as_float = models.FloatField(blank=True, null=True)




class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.CASCADE)
    amido = models.FloatField(null=True, default=0, blank=True)
    calorie = models.FloatField(null=True, default=0, blank=True)
    glucidi = models.FloatField(null=True, default=0, blank=True)
    proteine = models.FloatField(null=True, default=0, blank=True)
    lipidi = models.FloatField(null=True, default=0, blank=True)

    active= models.BooleanField(default=False)
    stock = models.OneToOneField(IngredientStock, related_name='ingredients', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'ingredients'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse("food:ingredient-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name

