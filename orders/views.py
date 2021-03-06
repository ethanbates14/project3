from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Categories,Options,Menu,Topping,Prices,Orders

# Orders Views
def index(request):

    if request.method == "POST":
        return render(request, "orders/checkout.html")

    else:
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

    context = {
        "data": food_items
    }
    return render(request, "orders/index.html", context)

def checkout(request):
    current_user = request.user
    orderdetails = Orders.objects.filter(user_id = current_user.id)

    context = {
        "myorders": orderdetails
    }

    if request.method == "POST":
        orderdetails.filter(order_status = 'P').update(order_status = 'C')
        return render(request, "users/user.html",context)
    else:
        orderdetails.filter(order_status = 'P')


    return render(request, "orders/checkout.html",context)