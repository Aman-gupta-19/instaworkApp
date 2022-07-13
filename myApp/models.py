import email
from unicodedata import name
from django.db import models

# Create your models here.

class TeamModel(models.Model):
    fname = models.CharField(max_length=50, default="random")
    lname = models.CharField(max_length=50, default="random")
    pno = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, default="random")
    role = models.IntegerField(default=0)


    def __str__(self):
        return self.fname