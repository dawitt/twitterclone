from django.http.response import HttpResponseRedirect
from tweet import models
from tweet.models import Tweet
from django import forms
from django.shortcuts import render
from tweet.forms import PostTweetForm

# Create your views here.

def post_tweet(request):
    if request.method == "POST":
        form = PostTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body =data['body'],
                author = request.user
            )
            return HttpResponseRedirect("/")
    form = PostTweetForm()
    return render(request, 'post.html', {'form': form})