
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'



    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    amido = models.FloatField(null=True, default=0)
    calorie = models.FloatField(null=True, default=0)
    glucidi = models.FloatField(null=True, default=0)
    proteine = models.FloatField(null=True, default=0)
    lipidi = models.FloatField(null=True, default=0)
    amido = models.FloatField(null=True, default=0)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'ingredients'


    def __str__(self):
        return self.name
