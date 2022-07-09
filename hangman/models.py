from django.db import models

# Create your models here.
class Word(models.Model):
    word= models.CharField(max_length=16)
    
    def __str__(self):
        return f"{self.word}"