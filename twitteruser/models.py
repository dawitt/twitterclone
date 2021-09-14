from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TweeterUser(AbstractUser):
    followers = models.ManyToManyField("self", blank=True, symmetrical=False)
    bio = models.CharField(max_length=100, null=True, blank=True)

def __str__(self):
    return self.follower
