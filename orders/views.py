from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Categories,Options,Menu,Topping,Prices

# Orders Views
def index(request):

    #build data array
    pin_category = Categories.objects.all()
    pin_foods = Menu.objects.all()
    pin_prices = Prices.objects.all()
    pin_topping = Topping.objects.all()

    food_items = {}

    for cg in pin_category:
    	food_items[cg.category_name] = []
    	query_menu = pin_foods.filter(category_id = cg.id)
    	for fd in query_menu:
    		menu_to_qs = {}
    		query_topping = pin_topping.filter(option_type_id = fd.menu_options_id)
    		query_prices = pin_prices.filter(menu_id = fd.id)
    		opt_dict = {'toppings': query_topping, 'prices': query_prices}
    		menu_to_qs[fd.menu_item] = opt_dict
    		food_items[cg.category_name].append(menu_to_qs)
    		#print(food_items)

    context = {
        "data": food_items
    }

    return render(request, "orders/index.html", context)
