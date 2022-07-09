from django.shortcuts import render
from django.http import HttpResponse
from .models import Word



# Create your views here.

w = Word.objects.first().__str__()


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def index(request):
    return render(request,"hangman/index.html",{'letters':letters , 'word':w})
