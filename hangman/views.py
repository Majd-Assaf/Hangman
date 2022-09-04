from os import stat
import random
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Word,Player,Game
from django.contrib.auth.models import User



# Create your views here.




letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s = Word.objects.first()


def index(request):        
    return render(request,"hangman/index.html")

def newGame(request):
    if request.method == 'POST':
        lsPlayerGames = [] 
        gCount = 0
        name = request.POST['username']
        players = Player.objects.all()
        player = Player()
        for p in players:
            if p.userName == name:
                player = Player.objects.get(userName = name)
                lsPlayerGames = Game.objects.filter(player = player)
                
        if player is None:
            user = Player(name)
            user.save()
    
    if lsPlayerGames.count() > 0 :
        gCount = lsPlayerGames.count()
        
            
    gameWord = "?"
    words=[]
    word = Word.objects.all()
    for w in word:
        words.append(w.word)
    w = random.randint(0,len(words) -1)
    gameWord = words[w]
    
    return render(request,"hangman/game.html",{'letters':letters, 'word':gameWord, 'gamesCount':gCount,'playerName':name , 'request':request})
    

def savegame(request,name, duration, tries, state):
    #hier where you save the game in th db
    #ask for new game
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     duration = request.POST["duration"]
    #     tries = request.POST["tries"]
    #     state = request.POST["state"]
    #     return render(request, "index.html", {
    #             "message": name
    #     })
    player = Player.objects.get(userName = name)
    game = Game()
    game.player = player
    game.duration = duration
    game.tryes = tries
    game.result = state
    game.save()
    
    lsPlayerGames = Game.objects.filter(player = player)
    
    return HttpResponse(lsPlayerGames)
    
      

    
