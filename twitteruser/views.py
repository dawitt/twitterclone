from django.shortcuts import render, HttpResponseRedirect
from twitteruser.models import TweeterUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    tweets = Tweet.objects.filter().order_by("-posted_at")
    return render(request, 'index.html', {'tweets': tweets})

def profile(request, id):
    author = TweeterUser.objects.get(id=id)
    tweet = Tweet.objects.filter(author=author).order_by("-posted_at")
    return render(request, 'profile.html', {'author':author, 'tweet':tweet})

