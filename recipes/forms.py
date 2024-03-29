from django.forms import forms

from recipes.models import Recipe, RecipeLine

from django import forms

from .models import Recipe, RecipeIngredient

"""
you can reneder fiel not i the model es calculation
"""
class RecipeForm(forms.ModelForm):
   
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": "Recipe Name"}))
    directions = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control" ,"rows": 6, "placeholder": "Directions"}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control" ,"rows": 3, "placeholder": "Description"}))
    active = forms.BooleanField(initial=False)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions', 'servings', 'active']
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].label='h'
    #     self.fields['name'].widget.attrs.update({'class': 'form-control-2'})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']

class RecipeLineForm(forms.ModelForm):
    class Meta:
        model = RecipeLine
        fields = ['name', 'directions', 'recipe']

