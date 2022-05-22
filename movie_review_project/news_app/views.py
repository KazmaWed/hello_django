from datetime import date
from django.shortcuts import render
from .models import News

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'newss.html',{'newss':newss})