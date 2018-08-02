from django.urls import path

from . import views

urlpatterns = [
    path("menu/", views.index, name="menu"),
    path("checkout/" , views.checkout, name="checkout")
]
