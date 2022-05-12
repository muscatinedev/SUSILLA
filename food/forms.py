from django import forms
from .models import Ingredient, Category, IngredientStock


class IngredientForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      queryset=Category.objects.all())

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": " Name"}))

    class Meta:
        model = Ingredient

        fields = [
            'category',
            'name',
            'calorie',
            'glucidi',
            'proteine',
            'lipidi',
            'amido',
            'active',



        ]

class StockForm(forms.ModelForm):
    class Meta:
        model = IngredientStock
        fields = ['quantity_as_float','min_quantity_as_float',



        ]
