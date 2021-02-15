from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home_list (request):
    web = models.Web.objects.all().order_by('date')
    arge = {'web':web}
    return render(request , 'web/home.html',arge)


def weblink(request,slug):
    web = models.Web.objects.get(slug=slug)
    return render(request, 'web/web_details.html',{'web':web})
def m001(request):
    return render(request, 'web/m001.html')
