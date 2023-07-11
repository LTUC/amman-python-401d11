from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255,help_text="Name of the thing you want to add")
    rank = models.IntegerField()
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc = models.TextField(default="no desc available")


    def __str__(self):
        return self.name
    

