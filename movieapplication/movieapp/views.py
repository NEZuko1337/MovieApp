from django.shortcuts import render


def home(request):
    return render(request, 'movieapp/home.html')


def advice_film(request):
    return render(request, 'movieapp/advice_film.html')