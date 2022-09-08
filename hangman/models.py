from datetime import date
from time import time
from django.db import models

# Create your models here.
class Word(models.Model):
    word= models.CharField(max_length=16)
    
    def __str__(self):
        return f"{self.id, self.word}"
    
class Player(models.Model):
    userName = models.CharField(max_length=8,unique=True)
    
    def __str__(self):
        return f"{self.id, self.userName}"
    
class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    duration = models.CharField(max_length=5)
    attempts = models.CharField(max_length=4)
    rightAttempts = models.CharField(max_length=4)
    wrongAttempts = models.CharField(max_length=4)
    date = models.DateTimeField()
    result = models.CharField(max_length=4)
    
    def __str__(self):
        return f"{self.id, self.player, self.duration, self.attempts, self.date, self.result}"