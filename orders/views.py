from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Categories, Menu, Prices

# Orders Views
def index(request):

    #build data array
    pin_category = Categories.objects.all()
    pin_foods = Menu.objects.all()
    pin_prices = Prices.objects.all()

    food_items = {}

    for cg in pin_category:
	    food_items[cg.category_name] = []
	    query_menu = pin_foods.filter(category_id = cg.id)
	    for fd in query_menu:
		    new_dict = {}
		    query_prices = pin_prices.filter(menu_id  = fd.id)
		    new_dict[fd.menu_item] = query_prices
		    food_items[cg.category_name].append(new_dict)
		    #print(food_items)

    context = {
        "data": food_items
    }

    return render(request, "orders/index.html", context)
