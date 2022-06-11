from django import forms
from .models import Supplier


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
