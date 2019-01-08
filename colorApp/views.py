from django.http import HttpResponse
from django.shortcuts import render

colorList = ["purple", "red", "blue", "green"]


def list(request):
    return render(request, 'colorApp/colorlist.html', {'colors': colorList})


def add(request):
    color = request.GET.get('newcolor')
    if color in colorList:
        return render(request, 'colorApp/409.html', status=409)
    else:
        colorList.append(color)
        return render(request, 'colorApp/colorlist.html', {'colors': colorList}, status=201)


def get(request):
    color = request.GET.get('color')
    if color in colorList:
        return HttpResponse("{}".format(color))
    else:
        return render(request, 'colorApp/404.html', status=404)


def index(request):
    return HttpResponse("Welcome to colors app")

