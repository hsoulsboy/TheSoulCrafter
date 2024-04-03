from django.db import models

# Create your models here.
class Character(models.Model):    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.FloatField()
    gender = models.CharField(max_length=1, default="M")
    weight = models.FloatField()
    
    def __str__(self) -> str:
        return self.name
    
class Personality(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    motivation = models.CharField(max_length=250)
    secrets = models.CharField(max_length=250)
    principles = models.CharField(max_length=250)
    
    def __str__(self)  -> str:
        return self.motivation
    
class Origin(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    ancestry = models.CharField(max_length=250)
    race = models.CharField(max_length=100)
    occupation = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.ancestry