from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Categories, Menu, Prices

# Orders Views
def index(request):
    context = {
        "food_cat": Categories.objects.all(),
        "menu": Menu.objects.all()
    }
    return render(request, "orders/index.html", context)
