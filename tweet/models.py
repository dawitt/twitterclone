from django.db import models
from django.forms.utils import to_current_timezone
from twitteruser.models import TweeterUser
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    body= models.CharField(max_length=140)
    author = models.ForeignKey(TweeterUser, on_delete=models.CASCADE, related_name='author')
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
    