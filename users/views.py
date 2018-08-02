from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# users views

def index_user(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index_user"))
        else:
            return render(request, "users/error.html", {"message": "Invalid credentials.", "backto": "login"})
    else:
        return render(request, "users/login.html", {"message": None})

def register_view(request):
    if request.method == "POST":
        u_firstname = request.POST.get('firstname')
        u_lastname = request.POST.get('lastname')
        u_email = request.POST.get('email')
        u_uname = request.POST.get('username')
        u_pwd = request.POST.get('password')

        #check if user exists
        userlist = User.objects.all()
        namecheck = userlist.filter(username = u_uname)
        emailcheck = userlist.filter(email = u_email)

        if namecheck:
            return render(request, "users/error.html", {"message": "Username already exists!", "backto": "register"})
        elif emailcheck:
            return render(request, "users/error.html", {"message": "Email already exists!", "backto": "register"})
        else:
            newuser = User.objects.create_user(u_uname, u_email, u_pwd)
            newuser.first_name = u_firstname
            newuser.last_name = u_lastname
            newuser.save()
            return render(request, "users/login.html")
    else:
        return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html")

def user_home(request):
    return render(request, "users/user.html")