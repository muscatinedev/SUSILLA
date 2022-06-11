from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory  # model form for querysets
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .forms import RecipeForm, RecipeIngredientForm, RecipeLineForm
from .models import Recipe, RecipeIngredient, RecipeLine
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

from main.utils import (
    convert_to_qty_units,
    parse_paragraph_to_recipe_line
)


# CRUD -> Create Retrieve Update & Delete


@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }

    print(User)
    return render(request, "recipes/list.html", context)

def recipe_active_list(request ):
    qs = Recipe.objects.filter(active=True)
    context = {
        "object_list": qs
    }

    print(User)
    return render(request, "recipes/list.html", context)


@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, pk=id, user=request.user)
    context = {
        "object": obj
    }

    return render(request, "recipes/detail.html", context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)

    # create the clsaa

    # Formset = modelformset_factory(Model, form=ModelForm, extra=0)
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient,
                                                   form=RecipeIngredientForm,
                                                   extra=0)
    qs = obj.recipeingredient_set.all()
    # create instance
    formset = RecipeIngredientFormset(request.POST or None,
                                      queryset=qs)
    context = {
        "form": form,
        "formset": formset,
        "object": obj,
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form2 in formset:
            child = form2.save(commit=False)
            child.recipe = parent
            child.save()

        context['message'] = 'Data Saved'

        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)

def line_create_view(request):
    form = RecipeLineForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        #return redirect(obj.get_absolute_url())
    return render(request, "recipes/create_line.html", context)

def recipe_line_view(request, id=None):
    recipe = get_object_or_404(Recipe, pk=id )
    lines= RecipeLine.objects.filter(recipe=recipe)
    context = {
        "recipe": recipe,
        "lines":lines
    }

    print(lines)
    return render(request, "recipes/lines.html", context)
