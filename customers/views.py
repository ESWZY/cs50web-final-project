from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        print(1234567890)
        return render(request, "customers/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "customers/user.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("customers:index"))
    else:
        return render(request, "customers/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "customers/login.html", {"message": "Logged out."})
