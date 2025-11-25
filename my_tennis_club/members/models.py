from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  video_game_favorite = models.CharField(max_length=100)
  amd_intel = models.CharField(max_length=255, null=True)
  music_favorite=models.BooleanField(max_length=255)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"  
  