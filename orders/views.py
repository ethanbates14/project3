from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Categories, Menu, Prices

# Orders Views
def index(request):

    #build data array
    pin_category = Categories.objects.all()
    pin_foods = Menu.objects.all()
    food_items = []

    for item in pin_category:
        food_items.append(item.category_name)
        query_item = pin_foods.filter(category_id = item.id)
        print(query_item)
        print(food_items)


    context = {
        "food_categories": Categories.objects.all(),
        "menu": Menu.objects.all()
    }
    return render(request, "orders/index.html", context)
