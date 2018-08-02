from django.urls import path

from . import views

# users urls
urlpatterns = [
    path("", views.index_user, name="index_user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("user", views.user_home, name="user_home")

]
