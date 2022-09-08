import datetime
import random
from django.shortcuts import render
from .models import Word,Player,Game
from django.contrib.auth.models import User



# Create your views here.




letters = ['A','Ä','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Ö','P','Q','R','S','T','U','Ü','V','W','X','Y','Z']

def index(request):        
    return render(request,"hangman/index.html")

def newGame(request):
    if request.method == 'POST':
        name = request.POST['username']
        isTime = request.POST.get('isTimeCounted', False)
        players = Player.objects.all()
        player = Player()
        for p in players:
            if p.userName == name:
                player = Player.objects.get(userName = name)
        if player is not None:
            player.userName= name
            player.save()
            
    gameWord = ""
    words=[]
    word = Word.objects.all()
    for w in word:
        words.append(w.word)
    w = random.randint(0,len(words) -1)
    gameWord = words[w]
    
    return render(request,"hangman/game.html",{'letters':letters, 'word':gameWord, 'isTimeCounted':isTime,'playerName':name})
    

def savegame(request):
    if request.method == 'POST':
        
        name = request.POST['username']
        duration =request.POST.get('duration','0')
        attempts = request.POST.get('attempts','0')
        result =request.POST.get('result','NO Info')
        rightAttempts = request.POST.get('rightAttempts','0')
        isTimeCounted = request.POST.get('isTimeCounted', False)

        players = Player.objects.all()
        player = Player()
        for p in players:
            if p.userName == name:
                player = Player.objects.get(userName = name)
        
        duration = 29 - int(duration)
        wrongAttempts = int(attempts) - int(rightAttempts)
        
        if isTimeCounted != False :
            isTimeCounted ='time count mode'
        else:
            isTimeCounted ='no time mode'
            duration= '0'
        
                
        game = Game()
        game.player = player
        game.duration = str(duration)
        game.attempts = attempts
        game.rightAttempts = rightAttempts
        game.wrongAttempts = str(wrongAttempts)
        game.date = datetime.datetime.now()
        game.result = result
        if game is not None:
           game.save()
        
        
        lsPlayerGames = []
        PlayerGames = Game.objects.filter(player = player)
        
        for game in PlayerGames:
            lsPlayerGames.append(game)
        
        return render(request,"hangman/index.html", {
            'games':lsPlayerGames,
            'name':name,
            'result':result,
            'isTimeCounted':isTimeCounted
        })
    
      

    
