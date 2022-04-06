from django import forms
from .models import Ingredient, Category

class IngredientForm(forms.ModelForm):
    class Meta:
        model= Ingredient

        fields =[
            'category',
            'name',
            'calorie',
            'glucidi',
            'proteine',
            'lipidi',
            'amido',


        ]
        
