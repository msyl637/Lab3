from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "templates/index.html")


def hello(request):
    return HttpResponse("Добро пожаловать в гостиницу «Комфорт»!")


def static_page(request):
    return render(request, "templates/static_handler.html")
