from django.shortcuts import render
from car.models import Car
from django.template import Context,loader
from django.http import HttpResponse
def index(request):
    car_list = Car.objects.all()
    l = loader.get_template("car/index.html")
    b = Context({"car_list":car_list,})
    return HttpResponse(l.render(b))