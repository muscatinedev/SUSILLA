from django.contrib.auth.models import User
from django.db import models

from main.validators import validate_unit_of_measure

from django.db import models



class Unit(models.Model):
    name = models.CharField(max_length=100, db_index=True, validators=[validate_unit_of_measure], blank=True, null=True)

    # name = models.CharField(max_length=50, validators=[validate_unit_of_measure], blank=True, null=True)

    class Meta:
        verbose_name_plural = 'units'

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=256)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    complete= models.BooleanField(default=False)



    def __str__(self):
        return self.name
