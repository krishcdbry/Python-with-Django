from django.shortcuts import render
from cdbry.models import Cdbry
from django.http import HttpResponse
from django.template import Context,loader
def index(request):
    cdbry_list = Cdbry.objects.all()
    l = loader.get_template("cdbry/index.html")
    c = Context({'cdbry_list':cdbry_list,})
    return HttpResponse(l.render(c))

