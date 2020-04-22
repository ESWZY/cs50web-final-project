from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Customer


# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("customers:index"))
        else:
            return render(request, "login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})


@login_required(login_url="customers:login")
def subscribe(request):
    try:
        if request.method == 'GET':
            if request.user.customer.sub:
                context = {"message": "You are already a subscriber!"}
                return render(request, "error.html", context)
            else:
                return render(request, "customers/subscribe.html")
        elif request.method == 'POST':
            money = request.POST['money']
            customer = request.user.customer
            if int(money) > customer.card_balance:
                return HttpResponse("Your account do not have enough money yet, please recharge.")
            else:
                customer.card_balance -= int(money)
                customer.sub = True
                customer.save()
                return HttpResponse("Congratulations! You are a subscriber now!")
        else:
            return render(request, "error.html", context={"message": "Method is not allowed!"})
    except:
        return render(request, "error.html", context={"message": "Please go to shop to recharge first!"})


@login_required(login_url="customers:login")
def shop(request):
    User()
    if request.method == 'GET':
        return render(request, "customers/shop.html")
    elif request.method == 'POST':
        cc = request.POST['cc']
        money = request.POST['money']
        phone = request.POST['phone']
        if 16 > len(cc) > 19:
            return render(request, "error.html", context={"message": "Check your credit card number length!"})
        try:
            customer = request.user.customer
            customer.credit_card = cc
            customer.card_balance += int(money)
            customer.save()
        except:
            customer = Customer()
            customer.username = request.user
            customer.credit_card = cc
            customer.card_balance = int(money)
            customer.save()
        return HttpResponseRedirect(reverse("customers:subscribe"))
    else:
        return render(request, "error.html", context={"message": "Method is not allowed!"})
