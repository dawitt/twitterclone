from django.shortcuts import redirect, render, HttpResponseRedirect
from twitteruser.models import TweeterUser
from tweet.models import Tweet



def tweet_detail(request, id):
    # author = TweeterUser.objects.get(id=id)
    tweet = Tweet.objects.get(id=id)

    return render(request, 'tweet_detail.html', {'tweet':tweet,})
