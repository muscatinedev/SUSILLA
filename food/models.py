from django.db import models

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.CASCADE)
    amido = models.FloatField(null=True, default=0)
    calorie = models.FloatField(null=True, default=0)
    glucidi = models.FloatField(null=True, default=0)
    proteine = models.FloatField(null=True, default=0)
    lipidi = models.FloatField(null=True, default=0)
    amido = models.FloatField(null=True, default=0)
    active= models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'ingredients'
        ordering = ('name',)

    def __str__(self):
        return self.name


class IngredientStock(models.Model):
    quantity_as_float = models.FloatField(blank=True, null=True)
    min_quantity_as_float = models.FloatField(blank=True, null=True)
    ingredient = models.OneToOneField(Ingredient, related_name='ingredients', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
