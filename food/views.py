import time
import pint

from django.shortcuts import render, get_object_or_404
from django.views.generic.list import   ListView
from django.views.generic.detail import DetailView
import openpyxl
from openpyxl import Workbook, load_workbook
from food.models import Category, Ingredient
from .forms import IngredientForm, StockForm


class CategoryListView(ListView):
    model = Category
    template_name = 'food/categories.html'


def food_main_view(request):
    categories = Category.objects.all()
    context ={'categories': categories}
    return render(request, 'food/food.html', context)

def category_detail_view(request, id):
    obj = get_object_or_404(Category, pk=id)
    ings= Ingredient.objects.filter(category=obj)

    context = {    "object": obj,
                   'ings':ings, }

    return render(request, "food/category_detail.html", context)






def impcat(request):
    wb = load_workbook('/home/matte/DEVELOPMENT/res/categories.xlsx')

    ws = wb.active
    for row in range(2,25):
        id= ws['A'+str(row)].value
        name=ws['B'+str(row)].value
        c = Category()


        c.name= name

        #c.save()
    ureg = pint.UnitRegistry()
    print(ureg['meters'])

    return render(request, 'food/food.html', {})


def imping(request):
    wb = load_workbook('/home/matte/DEVELOPMENT/res/ingred.xlsx')

    ws = wb.active
    for row in range(2,851):
        id= ws['A'+str(row)].value
        name=ws['B'+str(row)].value

        catid=ws['C'+str(row)].value
        am=ws['D'+str(row)].value
        cal=ws['E'+str(row)].value
        glu=ws['F'+str(row)].value
        pro=ws['G'+str(row)].value
        lip=ws['H'+str(row)].value

        cate = Category.objects.get(pk=catid)
        ing= Ingredient()
        ing.name=name
        ing.category=cate
        ing.amido=am
        ing.calorie=cal
        ing.glucidi=glu
        ing.proteine=pro
        ing.lipidi=lip

        time.sleep(0.01)

        print('saved {}'.format(ing))
      #  ing.save()
    return render(request, 'food/food.html', {})






def createCategory(request):
    return render(request, 'food/food.html', {})

def createIngredient(request):
    form = IngredientForm(request.POST or None)
    form2= StockForm(request.POST or None)
    if form.is_valid() and form2.is_valid():
        obj = form.save(commit=False)
        obj2 = form2.save(commit=False)
        obj2.ingredient = obj
        obj.save()
        obj2.save()

    return render(request, 'food/create_ing.html', {'form': form, 'form2':form2})
