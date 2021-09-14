from django.db import models
from twitteruser.models import TweeterUser
from tweet.models import Tweet 

# Create your models here.
class Notification(models.Model):
    notification = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    notifier = models.ForeignKey(TweeterUser, on_delete=models.CASCADE)
