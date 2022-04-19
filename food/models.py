from django.db import models

from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'

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

    class Meta:
        verbose_name_plural = 'ingredients'
        ordering = ('name',)


    def __str__(self):
        return self.name
