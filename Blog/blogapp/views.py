from django.shortcuts import render

from .models import *


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    maqolalar = Maqola.objects.all()
    return render(request, 'blog.html', {'maqolalar' : maqolalar})

def maqola(request, num):
    maqola1 = Maqola.objects.get(id = num)
    rasmlar = Rasm.objects.filter(maqola = maqola1)
    return render(request, 'maqola.html', {'maqola' : maqola1, 'rasmlar' : rasmlar})