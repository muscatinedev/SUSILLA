from django.shortcuts import render


def food_main_view(request):
    return render(request, 'food/food.html', {})


def createCategory(request):
    return render(request, 'food/food.html', {})
