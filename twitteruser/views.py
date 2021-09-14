from django.shortcuts import redirect, render, HttpResponseRedirect
from twitteruser.models import TweeterUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from tweet.forms import PostTweetForm
import re

# Create your views here.
@login_required
def index(request):
    tweets = Tweet.objects.filter().order_by("-posted_at")
    if request.method == "POST":
        form = PostTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet_body = Tweet.objects.create(
                body =data['body'],
                author = request.user
            )
        
            # if(Tweet.author.all() == re.findall(r"@\w+", data['body'])):
            #     print( Tweet.author)
            # print(re.findall(r"@\w+", data['body']) + "data['author']")
            return HttpResponseRedirect("/")
    form = PostTweetForm()
    return render(request, 'index.html', {'tweets': tweets, 'form': form, })

def profile(request, id):
    author = TweeterUser.objects.get(id=id)
    
    tweet = Tweet.objects.filter(author=author).order_by("-posted_at")
    tweet_numbers = len(tweet)
    followers = author.followers.all()
    total_followers = len(followers)
    if len(followers) == 0:
        is_following = False
    for follower in followers:
        if follower == request.user:
            is_following = True
            break
        else:
            is_following = False

    return render(request, 'profile.html', {'author':author, 
                                        'tweet':tweet,
                                        'tweet_numbers':tweet_numbers,
                                        'is_following':is_following,
                                        'total_followers':total_followers,
                                        })

def follower(request, id):
    profile = TweeterUser.objects.get(id=id)
    profile.followers.add(request.user)
    return redirect("profile", id=profile.id) 

def unfollow(request, id):
    profile = TweeterUser.objects.get(id=id)
    profile.followers.remove(request.user)
    return redirect("profile", id=profile.id) 