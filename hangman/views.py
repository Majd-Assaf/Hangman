from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

letters = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = ['d','e','u','t','s','c','h','l','a','n','d']

def index(request):
    return render(request,"hangman/index.html",{'letters':letters , 'word':word})
